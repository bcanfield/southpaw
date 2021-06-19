import requests


def get_fanduel_headers(xAuthToken, authorizationToken):
    headers = {'authority': 'api.fanduel.com',
               'accept': 'application/json',
               'x-auth-token': xAuthToken,
               'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
               'authorization': authorizationToken,
               'content-type': 'application/json',
               'origin': 'https://www.fanduel.com',
               'sec-fetch-site': 'same-site',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://www.fanduel.com/',
               'accept-language': 'en-US,en;q=0.9'
               }
    return headers


def get_players_in_contest(contest, xAuthToken, authorizationToken):
    fixtureListIds = contest['fixture_list']['_members']
    if len(fixtureListIds) > 0:
        fixtureListId = fixtureListIds[0]
        response = requests.get(
            "https://api.fanduel.com/fixture-lists/" + fixtureListId + "/players",
            headers=get_fanduel_headers(xAuthToken, authorizationToken))
        jsonData = response.json()
        return jsonData['players']


def get_upcoming_contests(userId, xAuthToken, authorization):
    # Get all upcoming rosters (duplicate/blank entries are grouped into one roster)
    headers = get_fanduel_headers(xAuthToken, authorization)
    response = requests.get(
        'https://api.fanduel.com/users/' + userId + '/rosters?status=upcoming',
        headers=headers)
    jsonData = response.json()
    upcomingContests = []
    # Dig through rosters to check if it is for correct sport
    for roster in jsonData['rosters']:
        rosterFixtureLists = roster['fixture_list']['_members']
        if len(rosterFixtureLists) > 0:
            rosterFixtureListId = rosterFixtureLists[0]
            for fixtureList in jsonData['fixture_lists']:
                if fixtureList['id'] == rosterFixtureListId:
                    if fixtureList['sport'] == 'UFC':
                        # Get all entries belonging to this roster
                        response = requests.get(
                            roster['grouped_entries']['_url'], headers=headers)
                        jsonDataNew = response.json()
                        for contest in jsonDataNew['contests']:
                            if not contest in upcomingContests:
                                upcomingContests.append(contest)
    return upcomingContests


def get_fighter_salaries(userId, xAuthToken, authorization):
    salary_list = []
    contests = get_upcoming_contests(userId, xAuthToken, authorization)
    # Use first ufc contest
    contest = contests[0]
    playerList = get_players_in_contest(contest, xAuthToken, authorization)
    for player in playerList:
        salary_list.append({'name': player['known_name'], 'salary': player['salary'],
                            'id': player['id'], 'imageUrl': player['images']['default']['url']})
    return salary_list
