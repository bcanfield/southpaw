![southpawgithub](https://user-images.githubusercontent.com/12603953/126020923-ea260184-ac3c-4960-bec3-0e68e3b89136.png)

[![Downloads](https://static.pepy.tech/badge/southpaw)](https://pypi.org/project/southpaw/)

**Southpaw** is a python package that provides access to the Fanduel API.

Optimize your DFS experience by programmatically retrieving and updating your lineups, analyzing your data, and more.

[API Documentation](https://bcanfield.github.io/southpaw/)
  
# Installation
```
python -m pip install southpaw
```

# Setup

  
**UPDATE (October 2023):**

**Fanduel has cracked down on automated methods of logging in and now requires two-factor auth - so this process now takes an extra initial step now to retrieve the auth headers.**

## How to retrieve your auth headers
1. Go to [Fanduel DFS](https://www.fanduel.com/contests) and log in.
2. Open up your browser inspector, toggle the Network tab, and refresh the page to view the requests.
4. You need to find one of the requests that is being sent to **https://api.fanduel.com**. Some examples are **fixture-lists?** and **current?**
5. In the **Response Headers** section, copy out the **Authorization** header and **X-Auth-Token**. Reference my screenshot below.

*Note: The x-auth-token expires. So you will have to repeat the method above when it does*

<img width="736" alt="Screenshot 2023-10-17 at 10 43 51 PM" src="https://github.com/bcanfield/southpaw/assets/12603953/b3a5f76b-6a87-4094-8fe6-e956072bfd2a">

## Start having fun 
You first must initialize your Fanduel object using your email, password, and auth tokens. You will see a success message if you succesfully authenticate.

```
import southpaw

basic_auth_token = 'Basic GBGskzdmGLKOP5EwMDNkNGUaLkFdM2VjKJHDNmY1Mjc6'
x_auth_token = 'eyasdffdsaasjhkdfbfkhdsbakjbasdkjfbnfkjdsaetgdffgdfdgs'
fanduel_email = 'fakeFanduelEmail@gmail.com'
fanduel_password = 'fakeFanduelPassword'

fd = southpaw.Fanduel(fanduel_email, fanduel_password, basic_auth_token, x_auth_token
```
You now have access to all of the data that Fanduel offers by using a rich set of helper functions that Southpaw provides.

## Examples

[Full Documentation](https://bcanfield.github.io/southpaw/)

It's easy to get overwhelmed with the amount of helper functions available and how to use them effectively.

See the **'Quick Start'** section below to get you up and running as quickly as possible.


## Quick Start
Get a list of all currently entered contests and all relevant info.

*FYI: If you are not entered into any Fanduel contests you will not get any back*
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
