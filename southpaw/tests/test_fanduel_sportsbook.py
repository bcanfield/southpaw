from southpaw.api.fanduel_sportsbook import *
import json
import os
from southpaw.tests import test_data_file_path


def test_get_all_fighters():
    assert(get_all_fighters())


def test_get_finish_odds():
    with open(test_data_file_path, 'r') as myfile:
        data = myfile.read()

    obj = json.loads(data)
    assert(get_finish_odds(obj))
