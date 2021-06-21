from southpaw.utilities import get_dates_of_saturday_and_sunday
import requests

fanduel_sportsbook_url = 'https://sportsbook.fanduel.com/cache/psmg/UK/50361.3.json'


def get_all_fighters(dates_to_search=get_dates_of_saturday_and_sunday()):
    """Retrieve a list of fighters and their available data from fanduel sportsbook.

    Args:
        dates_to_search (optional): A list of dates to search in the format: %Y-%m-%d. This will default to this Saturday and Sunday.

    Returns:
        A list of fighters from the sportsbook and some other provided data.
        Each fighter should be in the following format:

        {'name': 'Nate Diaz',
         'winOdds': 73,
         'eventNumber': 963382.3,
         'opponentName': 'Leon Edwards'}

        If there is no sportsbook data, an empty array will be returned
    """

    response = requests.get(fanduel_sportsbook_url, headers={
                            'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}, verify=False)
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


def get_finish_odds(fighter_list):
    """Retrieve finish odds for each fighter in a list.

    Args:
        fighter_list: A list of fighters, with each fighter containing at minimum 'eventNumber' and 'name'.

    Returns:
        The original list passed in, with each fighter object now containing 'finishOdds'.
    """
    for fighter in fighter_list:
        if(fighter['eventNumber']):
            # Create url to method odds
            method_odds_url = 'https://sportsbook.fanduel.com/cache/psevent/UK/1/false/' + \
                str(fighter['eventNumber']) + '.json'
            # Send method odds request
            method_response = requests.get(method_odds_url).json()
            # Extract data from method of victory json data
            if(method_response):
                if(method_response['eventmarketgroups']):
                    for event in method_response['eventmarketgroups']:
                        if event['name'] == 'All':
                            for method in event['markets']:
                                if method['name'] == 'Double Chance':
                                    for selection in method['selections']:
                                        if selection['name'] == fighter['name'] + ' by KO/TKO or Submission':
                                            # Calculate odds of a submission or K/O
                                            americanOdds = (
                                                selection['currentpriceup'] / selection['currentpricedown']) * 100
                                            if americanOdds < 0:
                                                americanOdds *= -1
                                            percentageOdds = americanOdds / \
                                                (americanOdds + 100)
                                            percentageOdds *= 100
                                            fighter['finishOdds'] = 100 - \
                                                percentageOdds
        else:
            fighter['finishOdds'] = 0
    return fighter_list
