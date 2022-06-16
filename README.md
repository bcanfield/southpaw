
  

  

  

![southpawgithub](https://user-images.githubusercontent.com/12603953/126020923-ea260184-ac3c-4960-bec3-0e68e3b89136.png)

  

  

  

[![Build Status](https://circleci.com/gh/bcanfield/southpaw/tree/main.svg?style=shield)](https://circleci.com/gh/bcanfield/southpaw/?branch=main)

  

  

[![PyPI pyversions](https://img.shields.io/pypi/v/southpaw)](https://pypi.python.org/pypi/southpaw/) [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

  

  

  

**Southpaw** is a python package that provides access to the Fanduel API.

  

  

Optimize your DFS experience by programmatically updating your lineups, analyzing your data, and more.

  

  

  

[Full Documentation](https://bcanfield.github.io/southpaw/)

  

  

  

## Installation

  

  

  

Install via [PyPi](https://pypi.org/project/southpaw/)

  

  

```

  

python -m pip install southpaw

  

```

  

  

  

## Initial Setup

  
**UPDATE (2022): Fanduel has cracked down on automated methods of logging in - so this process takes an extra initial step now to retrieve the necessary headers.**
  

Retrieve your basic auth token by logging into fanduel.com and copying the authorization header and x-auth-header from the dev console. (Green boxes)


<img width="798" alt="Screen Shot 2022-06-16 at 2 58 17 PM" src="https://user-images.githubusercontent.com/12603953/174152698-d48f4b07-5b81-48d2-a8ab-daceb59ecb07.png"  width="600" height="450">


Initialize your Fanduel object using your Fanduel email, password, and auth token. Initializing the Fanduel object will send off a test request to ensure that you can succesfully authenticate.

  

  

```

  

import southpaw

  

  

basic_auth_token = 'Basic GBGskzdmGLKOP5EwMDNkNGUaLkFdM2VjKJHDNmY1Mjc6'


x_auth_token = 'eyasdffdsaasjhkdfbfkhdsbakjbasdkjfbnfkjdsaetgdffgdfdgs'
  

fanduel_email = 'fakeFanduelEmail@gmail.com'

  

fanduel_password = 'fakeFanduelPassword'

  

  

fd = southpaw.Fanduel(fanduel_email, fanduel_password, basic_auth_token, x_auth_token)

  

```

  

Next you need to get your upcoming data. This is the most important step. This will retrieve all entries that the current user has, along with the whole load of info that is available from Fanduel's API.

  

```

  

fd.get_upcoming()

  

```

  

Once you call this function, you now have access to all of the data that Fanduel offers by using a rich set of helper functions that Southpaw provides.

  

## Examples

  

[Full Documentation](https://bcanfield.github.io/southpaw/)

  

Get all upcoming entries

  

  

```

  

fd.get_entries()

  

```

  

  

Get all upcoming contests

  

  

```

  

fd.get_contests()

  

```

  Update a Fanduel Entry
```
# Get an entry
entry = fd.get_entry('entry_id')

available_players = fd.get_players_in_entry(this_entry.id)

# Decide what players to use. Here we are just grabbing the first 5 in the list as an example
players_to_use = available_players[:5]

update_entry_input = [UpdateEntryInput({'id': entry.id, 'lineup': players_to_use})]

fd.update_entries(update_entry_input)
```

  

## Disclaimer

  

This project is for educational use only.

  

Accumulating Fanduel points or prizes through unauthorized methods such as unauthorized scripts or other automated means is against the Fanduel terms and may result in account disqualification.

The contributors of Southpaw shall not be held responsible for any actions taken using this tool.
