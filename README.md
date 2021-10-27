
  

  

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

  

Retrieve your basic auth token by logging into the Fanduel UI and copying the authorization header from the dev console.

  

Initialize your Fanduel object using your Fanduel email, password, and auth token.

  

```

import southpaw

  

basic_auth_token = 'Basic GBGskzdmGLKOP5EwMDNkNGUaLkFdM2VjKJHDNmY1Mjc6'

fanduel_email = 'fakeFanduelEmail@gmail.com'

fanduel_password = 'fakeFanduelPassword'

  

fd = southpaw.Fanduel(fanduel_email, fanduel_password, basic_auth_token)

```

Next you need to get your upcoming data. This is the most important step. This will retrieve all entries that the current user has, along with the whole load of info that is available from Fanduel's API.

 
```

fd.get_upcoming()

```

Once you call this function, you now have access to all of the data that Fanduel offers by using a rich set of helper functions that Southpaw provides.
  

## Example Fanduel Functions

[Full Documentation](https://bcanfield.github.io/southpaw/)

Get all of the current user's upcoming data

  

```

fd.get_upcoming()

```

  

Get all upcoming entries

  

```

fd.get_entries()

```

  

Get all upcoming contests

  

```

fd.get_contest()

```

Get all players in a given entry

  

```

fd.get_players_in_entry(entry_id)

```

## Disclaimer

This project is for educational use only.

Accumulating Fanduel points or prizes through unauthorized methods such as unauthorized scripts or other automated means is against the Fanduel terms and may result in account disqualification.

The contributors of Southpaw shall not be held responsible for any actions taken using this tool.