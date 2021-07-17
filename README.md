
![southpawgithub](https://user-images.githubusercontent.com/12603953/126020923-ea260184-ac3c-4960-bec3-0e68e3b89136.png)

[![Build Status](https://circleci.com/gh/bcanfield/southpaw/tree/main.svg?style=shield)](https://circleci.com/gh/bcanfield/southpaw/?branch=main)
[![PyPI pyversions](https://img.shields.io/pypi/v/southpaw)](https://pypi.python.org/pypi/southpaw/) [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

**Southpaw** is a python package that provides access to the Fanduel API, Fanduel Sportsbook, and custom lineup optimizers.  

[Documentation](https://bcanfield.github.io/southpaw/)

## Installation

Install via [PyPi](https://pypi.org/project/southpaw/)
```
python -m pip install southpaw
```

## Example Usage
Authenticate with Fanduel
```
southpaw.get_x_auth_token_and_user_id(email, password)
```
Create headers with your auth token
```
southpaw.get_fanduel_headers_with_x_auth(x_auth_token, basic_auth_token)
```
Get all upcoming contest for a user
```
southpaw.get_upcoming_contests(user_id, fanduel_headers, sport='any')
```