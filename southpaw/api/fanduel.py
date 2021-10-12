import requests


class Player():
    def __init__(self, player_json):
        self.dvp_rank = player_json['first_name']
        self.first_name = player_json['first_name']
        self.fppg = player_json['fppg']
        self.id = player_json['id']
        self.fixture = player_json['fixture']
        self.images = player_json['images']
        self.injured = player_json['injured']
        self.injury_details = player_json['injury_details']
        self.injury_severity = player_json['injury_severity']
        self.injury_status = player_json['injury_status']
        self.jersey_number = player_json['jersey_number']
        self.known_name = player_json['known_name']
        self.last_name = player_json['last_name']
        self.max_rank = player_json['max_rank']
        self.news = player_json['news']
        self.played = player_json['played']
        self.news = player_json['news']
        self.player_card_url = player_json['player_card_url']
        self.player_info = player_json['player_info']
        self.position = player_json['position']
        self.positions = player_json['positions']
        self.projected_fantasy_points = player_json['projected_fantasy_points']
        self.projected_starting_order = player_json['projected_starting_order']
        self.rank = player_json['rank']
        self.recent_games_played_stats = player_json['recent_games_played_stats']
        self.removed = player_json['removed']
        self.roster_position_stats = player_json['roster_position_stats']
        self.salary = player_json['salary']
        self.sport_specific = player_json['sport_specific']
        self.starting_order = player_json['starting_order']
        self.swappable = player_json['swappable']
        self.team = player_json['team']
        self.tier = player_json['tier']
        self.videos = player_json['videos']


class Contest():
    def __init__(self, contest_json):
        self.id = contest_json["id"]
        self._url = contest_json["_url"]
        self.invite_url = contest_json["invite_url"]
        self.sport = contest_json["sport"]
        self.name = contest_json['name']
        self.display_name = contest_json['display_name']
        self.label = contest_json['label']
        self.salary_cap = contest_json['salary_cap']
        self.start_date = contest_json['start_date']
        self.entry_fee = contest_json['entry_fee']
        self.entry_fee_fdp = contest_json['entry_fee_fdp']
        self.guaranteed = contest_json['guaranteed']
        self.max_entries_per_user = contest_json['max_entries_per_user']
        self.private = contest_json['private']
        self.made_free = contest_json['made_free']
        self.prizes = contest_json['prizes']
        self.fixture_list = contest_json['fixture_list']
        self.entries = contest_json['entries']
        self.size = contest_json['size']
        self.user_created = contest_json['user_created']
        self.h2h = contest_json['h2h']
        self.started = contest_json['started']
        self.final = contest_json['final']
        self.cancellation = contest_json['cancellation']
        self.features = contest_json['features']
        self.notice = contest_json['notice']
        self.score_to_beat = contest_json['score_to_beat']
        self.score_to_beat_pot = contest_json['score_to_beat_pot']
        self.season_long_info = contest_json['season_long_info']
        self.draft_specification = contest_json['draft_specification']


class Entry():
    def __init__(self, entry_json):
        self.id = entry_json["id"]
        self._url = entry_json["id"]
        self.entry_currency = entry_json["entry_currency"]
        self.cancelable = entry_json["cancelable"]
        self.index = entry_json["index"]
        self.rank = entry_json["rank"]
        self.user = entry_json["user"]
        self.has_lineup = entry_json["has_lineup"]
        self.fixture_list = entry_json["fixture_list"]
        self.contest = entry_json["contest"]
        self.prizes = entry_json["prizes"]
        self.roster = entry_json["roster"]
        self.code = entry_json["code"]


class UserAuth():
    def __init__(self, user_id, session_token, basic_auth_token):
        self.user_id = user_id
        self.session_token = session_token
        self.basic_auth_token = basic_auth_token


def login(fanduel_email, fanduel_password, basic_auth_token):
    """Get session token and user id from the fanduel auth api

    Args:
        fanduel_email: Your fanduel email address
        fanduel_password: Your fanduel password
        basic_auth_token: Your static authorization header from Fanduel

    Returns:
        An UserAuth object to use on requests to the Fanduel API
    """
    body = {"email": fanduel_email,
            "password": fanduel_password, "product": "DFS"}
    sessions_response_json = requests.post(
        'https://api.fanduel.com/sessions',
        headers=get_fanduel_headers(basic_auth_token=basic_auth_token), json=body).json()
    if len(sessions_response_json['sessions']) > 0:
        # Succesfully grabbed token from response
        session_token = sessions_response_json['sessions'][0]['id']
        user_id = sessions_response_json['sessions'][0]['user']['_members'][0]
        return UserAuth(user_id, session_token, basic_auth_token)
    else:
        print('Error Logging in: ',
              sessions_response_json['error']['description'])
        return None


def get_fanduel_headers(user_auth=None, basic_auth_token=None):
    """Create headers for the fanduel api

    Args:
        user_auth (optional): Pass in a UserAuth object to create headers that have a session token (Necessary for almost all requests to the Fanduel API)
        basic_auth_token (optional): Pass in just a bearer token to create headers without a session token (This is used for logging in and getting the session token)

    Returns:
        The headers object to be used in all requests to the fanduel api
    """
    headers = {'authority': 'api.fanduel.com',
               'accept': 'application/json',
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
               'content-type': 'application/json',
               'origin': 'https://www.fanduel.com',
               'sec-fetch-site': 'same-site',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://www.fanduel.com/',
               'accept-language': 'en-US,en;q=0.9'
               }

    if(user_auth):
        headers['x-auth-token'] = user_auth.session_token
        headers['authorization'] = user_auth.basic_auth_token
    elif(basic_auth_token):
        headers['authorization'] = basic_auth_token
    return headers


def get_players_in_contest(user_auth, contest):
    """Get a list of players that are in a given contest.

    Args:
        user_auth: UserAuth object to authenticate with Fanduel API
        contest: A contest object retrieved from the fanduel api

    Returns:
        A list of players in the contest
    """
    fixture_list_ids = contest.fixture_list['_members']

    if len(fixture_list_ids) > 0:
        fixture_list_id = fixture_list_ids[0]
        players_response = requests.get(
            "https://api.fanduel.com/fixture-lists/" + fixture_list_id + "/players",
            headers=get_fanduel_headers(user_auth=user_auth)).json()
        return [Player(player) for player in players_response['players']]


def get_upcoming_contests(user_auth, sport='any'):
    """Get a list of upcoming contests for a given user.

    Args:
        user_id: Fanduel user id
        fanduel_headers: Valid headers for the fanduel api
        sport (optional): Specify sport to get contests for. Default is 'any'

    Returns:
        A list of upcoming contests for the user
    """

    fanduel_headers = get_fanduel_headers(user_auth=user_auth)
    # Get all upcoming rosters (duplicate/blank entries are grouped into one roster)
    rosters_response = requests.get(
        'https://api.fanduel.com/users/' + user_auth.user_id + '/rosters?status=upcoming',
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
                                upcoming_contests.append(Contest(contest))
    return upcoming_contests


def get_entries_in_contest(user_auth, contest_id):
    """Get a list of entries in an upcoming contest

    Args:
        user_id: Fanduel user id
        contest_id: The id of the contest to get entries for
        fanduel_headers: Valid headers for the fanduel api

    Returns:
        A list of entries
    """
    fanduel_headers = get_fanduel_headers(user_auth=user_auth)
    entries_response = requests.get(
        "https://api.fanduel.com/contests/" + contest_id +
        "/entries?user=" + user_auth.user_id + "&page=1&page_size=250",
        headers=fanduel_headers).json()
    entries = [Entry(entry) for entry in entries_response['entries']]

    for entry in entries:
        try:
            rosterId = entry['roster']['_members'][0]
        except Exception as e:
            rosterId = ''
        if rosterId != '':
            roster_response = requests.get(
                'https://api.fanduel.com/users/' + user_auth.user_id + '/rosters/' + rosterId,
                headers=fanduel_headers).json()
            entry.rosterDetails = roster_response['rosters'][0]['name']
    return entries
