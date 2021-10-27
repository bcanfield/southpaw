import json
from southpaw.fanduel import Fanduel


def test_fanduel():
    entries_file = open(
        'southpaw/tests/testData/testEntries.json',)
    entries_data = json.load(entries_file)

    players_file = open(
        'southpaw/tests/testData/testPlayers.json',)
    players_data = json.load(players_file)

    entries_data['player_lists'] = players_data['player_lists']
    fd = Fanduel('fakeEmail', 'fakePassword',
                 'fakeAuthToken', entries_data)

    fd.get_upcoming()
    assert len(fd.get_entries()) == 1
    assert len(fd.get_rosters()) == 1
    assert len(fd.get_contests()) == 1
    assert len(fd.get_fixtures()) == 1
    assert len(fd.get_fixture_lists()) == 1
    assert len(fd.get_game_descriptions()) == 1
    assert len(fd.get_player_lists()) == 1
