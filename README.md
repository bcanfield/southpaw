
  

  

  

![southpawgithub](https://user-images.githubusercontent.com/12603953/126020923-ea260184-ac3c-4960-bec3-0e68e3b89136.png)

  

  

  

[![Build Status](https://circleci.com/gh/bcanfield/southpaw/tree/main.svg?style=shield)](https://circleci.com/gh/bcanfield/southpaw/?branch=main)

  

  

[![PyPI pyversions](https://img.shields.io/pypi/v/southpaw)](https://pypi.python.org/pypi/southpaw/) [![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-360/)

  

  

  

**Southpaw** is a python package that provides access to the Fanduel API.

  

  

Optimize your DFS experience by programmatically retrieving and updating your lineups, analyzing your data, and more.

  

  

  

[Full Documentation](https://bcanfield.github.io/southpaw/)

  

  

  

## Installation

  

  

  

Install via [PyPi](https://pypi.org/project/southpaw/)

  

  

```

  

python -m pip install southpaw

  

```

  

  

  

## Initial Setup

  
**UPDATE (2023): Fanduel has cracked down on automated methods of logging in - so this process takes an extra initial step now to retrieve the necessary headers.**
  

Retrieve your basic auth token by logging into fanduel.com and copying the authorization header and x-auth-header from the dev console. (Green boxes)


<img width="798" alt="Screen Shot 2022-06-16 at 2 58 17 PM" src="https://user-images.githubusercontent.com/12603953/174152698-d48f4b07-5b81-48d2-a8ab-daceb59ecb07.png"  width="600" height="450">


<br></br>
Initialize your Fanduel object using your Fanduel email, password, and auth tokens. Initializing the Fanduel object will send off a test request to ensure that you can succesfully authenticate.  

```

import southpaw

  
basic_auth_token = 'Basic GBGskzdmGLKOP5EwMDNkNGUaLkFdM2VjKJHDNmY1Mjc6'

x_auth_token = 'eyasdffdsaasjhkdfbfkhdsbakjbasdkjfbnfkjdsaetgdffgdfdgs'
  
fanduel_email = 'fakeFanduelEmail@gmail.com'

fanduel_password = 'fakeFanduelPassword'

fd = southpaw.Fanduel(fanduel_email, fanduel_password, basic_auth_token, x_auth_token)

```



  

Once you call this function, you now have access to all of the data that Fanduel offers by using a rich set of helper functions that Southpaw provides.

  

## Examples

[Full Documentation](https://bcanfield.github.io/southpaw/)

It's easy to get overwhelmed with the amount of helper functions available and how to use them effectively.

See the **'Quick Start'** section below to get you up and running as quickly as possible.


## Quick Start
Get a list of all currently entered contests and all relevant info
```

# Get a list of all currently entered contests
contests = fd.easy_get_contests()

# Are we entered in any contests?
if len(contests) > 0:
    # Grab the first contest for now
    # You could filter by sport or name
    contest = contests[0]
    print("Contest: ", contest["name"], contest["sport"], contest["salary_cap"])
    
    # Get entries in this contest
    entries = contests[0]["entries"]
    
    for entry in entries:
        print("Entry: ", entry["id"])
        print("Entry Required Lineup Format:", fd.get_roster_format_in_entry(entry["id"]))
        
        # Get players available to choose for this entry
        print("Available Players: ", len(entry["available_players"]))

# From here we have the contest info, required lineup format, and available players.
# We have everything we need to smartly update some entries

# Just blindly taking first 5 players as an example
players_to_use = available_players[:5]
update_entry_input = [UpdateEntryInput({'id': entry["id"], 'lineup': players_to_use})]

```

  

## Disclaimer

  

This project is for educational use only.

  

Accumulating Fanduel points or prizes through unauthorized methods such as unauthorized scripts or other automated means is against the Fanduel terms and may result in account disqualification.

The contributors of Southpaw shall not be held responsible for any actions taken using this tool.
