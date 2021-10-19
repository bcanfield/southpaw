import json
from southpaw.fanduel import Fanduel


def test_fanduel():
    entries_file = open(
        'southpaw/tests/testData/testEntries.json',)
    entries_data = json.load(entries_file)

    players_file = open(
        'southpaw/tests/testData/testPlayers.json',)
    players_data = json.load(players_file)

    entries_data['players'] = players_data['players']
    fd = Fanduel('fakeEmail', 'fakePassword',
                 'fakeAuthToken', entries_data)

    fd.get_upcoming()
    assert len(fd.get_entries()) == 5
    assert len(fd.get_rosters()) == 5
    assert len(fd.get_contests()) == 5
    assert len(fd.get_fixtures()) == 16
    assert len(fd.get_fixture_lists()) == 5
    assert len(fd.get_game_descriptions()) == 5
    assert len(fd.get_players()) == 5
