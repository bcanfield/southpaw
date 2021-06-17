from southpaw.utilities import get_dates_of_saturday_and_sunday
import requests

sportsbook_url = 'https://sportsbook.fanduel.com/cache/psmg/UK/50361.3.json'


def get_fanduel_sportsbook_data(dates_to_search=get_dates_of_saturday_and_sunday()):
    response = requests.get(sportsbook_url)
    results = []

    for event in response.json()['events']:
        if event['tsstart'].split('T')[0] in dates_to_search:
            for market in event['markets']:
                for selection in market['selections']:
                    decimalOdds = selection['price']
                    impliedProbability = (1/decimalOdds) * 100
                    if selection['name'] == event['participantname_home']:
                        opponentName = event['participantname_away']
                    elif selection['name'] == event['participantname_away']:
                        opponentName = event['participantname_home']
                    else:
                        opponentName = 'None'
                    results.append(
                        {'name': selection['name'], 'winOdds': impliedProbability, 'eventNumber': event['idfoevent'], 'opponentName': opponentName})

    return results
