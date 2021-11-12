import json
from southpaw.fanduel import Fanduel, UpdateEntryInput
import unittest
from unittest import mock
import responses


@responses.activate
def test_get_upcoming():
    entries_file = open(
        'southpaw/tests/testData/testEntries.json',)
    entries_data = json.load(entries_file)

    players_file = open(
        'southpaw/tests/testData/testPlayers.json',)
    players_data = json.load(players_file)

    entries_data['player_lists'] = players_data['player_lists']
    responses.add(responses.POST, 'https://api.fanduel.com/sessions',
                  json={"sessions": [{"id": "testSessionToken", "user": {
                      "_members": [
                          "testUserId"
                      ]
                  }}]}, status=200)
    responses.add(responses.GET, 'https://api.fanduel.com/users/testUserId/entries?status=upcoming',
                  json=entries_data, status=200)
    responses.add(responses.GET, 'https://api.fanduel.com/fixture-lists/65522/players',
                  json=players_data['player_lists'][0], status=200)

    fd = Fanduel('fakeEmail', 'fakePassword',
                 'fakeAuthToken')

    fd.get_upcoming()
    assert len(fd.get_entries()) == 1
    assert len(fd.get_rosters()) == 1
    assert len(fd.get_contests()) == 1
    assert len(fd.get_fixtures()) == 1
    assert len(fd.get_fixture_lists()) == 1
    assert len(fd.get_game_descriptions()) == 1
    assert len(fd.get_player_lists()) == 1

    responses.add(responses.PUT, 'https://api.fanduel.com/users/testUserId/entries',
                  json={"_meta": {"operations": {"success_count": 1, "failure_count": 0}}}, status=200)

    first_entry = fd.get_entries()[0]
    available_players = fd.get_players_in_entry(first_entry.id)
    blh = UpdateEntryInput(
        {'id': first_entry.id, 'lineup': available_players.players[-5:]})
    print(blh.to_json())
    update_entries_response = fd.update_entries([UpdateEntryInput(
        {'id': first_entry.id, 'lineup': available_players.players[-5:]})])
    assert update_entries_response is not None
