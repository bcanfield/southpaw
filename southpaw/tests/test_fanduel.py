import southpaw


def test_get_upcoming():
    basic_auth_token = ''
    x_auth_token = ''
    fanduel_email = ''

    fanduel_password = ''

    fd = southpaw.Fanduel(
        fanduel_email, fanduel_password, basic_auth_token, x_auth_token)

    print(fd.get_upcoming())
    print(fd.get_entries())
    print(fd.get_entry(fd.get_entries()[0].id))
    print(fd.get_rosters())
    print(fd.get_roster(fd.get_rosters()[0].id))
    print(fd.get_contests())
    print(fd.get_contest(fd.get_contests()[0].id))
    print(fd.get_fixtures())
    print(fd.get_fixture(fd.get_fixtures()[0].id))
    print(fd.get_fixture_lists())
    print(fd.get_fixture_list(fd.get_fixture_lists()[0].id))
    print(fd.get_game_descriptions())
    print(fd.get_game_description(fd.get_game_descriptions()[0].id))
    print(fd.get_player_lists())
    print(fd.get_player_list(fd.get_fixture_lists()[0].id))
    print(fd.get_players_in_entry(fd.get_entries()[0].id))
    print(fd.get_roster_format_in_entry(fd.get_entries()[0].id))
