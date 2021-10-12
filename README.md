
  

![southpawgithub](https://user-images.githubusercontent.com/12603953/126020923-ea260184-ac3c-4960-bec3-0e68e3b89136.png)

  

[![Build Status](https://circleci.com/gh/bcanfield/southpaw/tree/main.svg?style=shield)](https://circleci.com/gh/bcanfield/southpaw/?branch=main)

[![PyPI pyversions](https://img.shields.io/pypi/v/southpaw)](https://pypi.python.org/pypi/southpaw/) [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

  

**Southpaw** is a python package that provides access to the Fanduel API.

Whether you are looking to optimize your betting experience or simply experiment with the features Fanduel offers, this is the perfect place to start.

  

[Full Documentation](https://bcanfield.github.io/southpaw/)

  

## Installation

  

Install via [PyPi](https://pypi.org/project/southpaw/)

```
python -m pip install southpaw
```

  

## Initial Setup

Retrieve your basic auth token by logging into the Fanduel UI

  
  
Initialize your Fanduel object using your Fanduel email, password, and auth token.

```
basic_auth_token = 'Basic GBGskzdmGLKOP5EwMDNkNGUaLkFdM2VjKJHDNmY1Mjc6'
fanduel_email = 'fakeFanduelEmail@gmail.com'
fanduel_password = 'fakeFanduelPassword'
  

fd = southpaw.Fanduel(fanduel_email, fanduel_password, basic_auth_token)
```
Authenticate with Fanduel. This sends your credentials to the Fanduel API in exchange for a session token. Your session token needs to be valid in order to send any other requests to the Fanduel API. You can call this function to start a new session at anytime.

```
fd.login()
```

## Fanduel Functions
Get all upcoming contests

```
contests = fd.get_upcoming_contests()
```

Get all players in a contest

```
fd.get_players_in_contest(contest)
```

Get all entries in a contest

```
fd.get_entries_in_contest(contest)
```