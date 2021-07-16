import requests


def get_x_auth_token_and_user_id(fanduel_email, fanduel_password):
    """Get x-auth-token and user id from the fanduel auth api

    Args:
        fanduel_email: Your fanduel email address
        fanduel_password: Your fanduel password

    Returns:
        An object with the format {'x-auth-token': 'YOUR AUTH TOKEN', 'userID': 'YOUR USER ID}
    """
    body = {"email": fanduel_email,
            "password": fanduel_password, "product": "DFS"}
    response = requests.post(
        'https://api.fanduel.com/sessions',
        headers=get_fanduel_headers_without_x_auth(fanduel_email, fanduel_password), json=body)
    jsonData = response.json()
    if len(jsonData['sessions']) > 0:
        # Succesfully grabbed token from response
        token = jsonData['sessions'][0]['id']
        userId = jsonData['sessions'][0]['user']['_members'][0]
        return {'x-auth-token': token, 'userId': userId}
    else:
        return None


def get_fanduel_headers_without_x_auth(basic_auth_token):
    """Create valid headers for the fanduel api, without x-auth-token

    Args:
        basic_auth_token: The bearer token used to verify each user connecting to the fanduel api

    Returns:
        The headers object to be used in the initial request to get the x-auth-token
    """
    headers = {'authority': 'api.fanduel.com',
               'accept': 'application/json',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
               'authorization': basic_auth_token,
               'content-type': 'application/json',
               'origin': 'https://www.fanduel.com',
               'sec-fetch-site': 'same-site',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://www.fanduel.com/',
               'accept-language': 'en-US,en;q=0.9'
               }
    return headers


def get_fanduel_headers_with_x_auth(x_auth_token, basic_auth_token):
    """Create valid headers for the fanduel api, including x-auth-token

    Args:
        x_auth_token: The x_auth_token used to verify each user connecting to the fanduel api
        basic_auth_token: The bearer token used to verify each user connecting to the fanduel api

    Returns:
        The headers object to be used in all requests to the fanduel api
    """
    headers = {'authority': 'api.fanduel.com',
               'accept': 'application/json',
               'x-auth-token': x_auth_token,
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
               'authorization': basic_auth_token,
               'content-type': 'application/json',
               'origin': 'https://www.fanduel.com',
               'sec-fetch-site': 'same-site',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://www.fanduel.com/',
               'accept-language': 'en-US,en;q=0.9'
               }
    return headers


def get_players_in_contest(contest, fanduel_headers):
    """Get a list of players that are in a given contest.

    Args:
        contest: A contest object retrieved from the fanduel api
        fanduel_headers: Valid headers for the fanduel api

    Returns:
        A list of players in the contest
    """
    fixture_list_ids = contest['fixture_list']['_members']
    if len(fixture_list_ids) > 0:
        fixture_list_id = fixture_list_ids[0]
        players_response = requests.get(
            "https://api.fanduel.com/fixture-lists/" + fixture_list_id + "/players",
            headers=fanduel_headers).json()
        return players_response['players']


def get_upcoming_contests(user_id, fanduel_headers, sport='any'):
    """Get a list of upcoming contests for a given user.

    Args:
        user_id: Fanduel user id
        fanduel_headers: Valid headers for the fanduel api
        sport (optional): Specify sport to get contests for. Default is 'any'

    Returns:
        A list of upcoming contests for the user
    """
    # Get all upcoming rosters (duplicate/blank entries are grouped into one roster)
    rosters_response = requests.get(
        'https://api.fanduel.com/users/' + user_id + '/rosters?status=upcoming',
        headers=fanduel_headers).json()
    upcoming_contests = []
    # Dig through rosters to check if it is for correct sport
    for roster in rosters_response['rosters']:
        roster_fixture_lists = roster['fixture_list']['_members']
        if len(roster_fixture_lists) > 0:
            roster_fixture_list_id = roster_fixture_lists[0]
            for fixture_list in rosters_response['fixture_lists']:
                if fixture_list['id'] == roster_fixture_list_id:
                    if fixture_list['sport'] == sport or sport == 'any':
                        # Get all entries belonging to this roster
                        entries_response = requests.get(
                            roster['grouped_entries']['_url'], headers=fanduel_headers).json()
                        for contest in entries_response['contests']:
                            if not contest in upcoming_contests:
                                upcoming_contests.append(contest)
    return upcoming_contests


def get_entries_in_contest(user_id, contest_id, fanduel_headers):
    """Get a list of entries in an upcoming contest

    Args:
        user_id: Fanduel user id
        contest_id: The id of the contest to get entries for
        fanduel_headers: Valid headers for the fanduel api

    Returns:
        A list of entries
    """
    entries_response = requests.get(
        "https://api.fanduel.com/contests/" + contest_id +
        "/entries?user=" + user_id + "&page=1&page_size=250",
        headers=fanduel_headers).json()
    entries = entries_response['entries']

    for entry in entries:
        roster = []
        try:
            rosterId = entry['roster']['_members'][0]
        except Exception as e:
            rosterId = ''
        if rosterId != '':
            roster_response = requests.get(
                'https://api.fanduel.com/users/' + user_id + '/rosters/' + rosterId,
                headers=fanduel_headers).json()
        entry['rosterDetails'] = roster_response['rosters'][0]['name']
    return entries


def get_fighter_salaries(user_id, x_auth_token, basic_auth_token):
    """Get a list of fighters in a user's upcoming fanduel contest with their fanduel salaries

    Args:
        user_id: Fanduel user id
        x_auth_token: The x_auth_token used to verify each user connecting to the fanduel api
        basic_auth_token: The bearer token used to verify each user connecting to the fanduel api

    Returns:
        A list of fighters containing salaries
    """
    fanduel_headers = get_fanduel_headers_with_x_auth(
        x_auth_token, basic_auth_token)
    contests = get_upcoming_contests(user_id, fanduel_headers)
    player_list = get_players_in_contest(contests[0], fanduel_headers)
    salary_list = [{'name': player['known_name'], 'salary': player['salary'],
                    'id': player['id'], 'imageUrl': player['images']['default']['url']} for player in player_list]
    return salary_list
