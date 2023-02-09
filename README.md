# TomServo

## Features

- TODO

## Requirements

- TODO

## Installation

- Checkout locally `git clone https://github.com/MattShirley/TomServo.git`
- Create an `.env` file in the same directory as README.md
- Add a variable `DISCORD_TOKEN` set to the value of your bot's Discord token
- Add a variable `CHANNEL_ID` set to the channel ID that you want your bot to talk in
- Make sure `poetry` is installed by running: `python -m pip install poetry`
- Make sure the `poetry` environment variable plugin is installed: `python -m poetry plugin add poetry-dotenv-plugin`
- Install app locally with `python -m poetry install`

Your `.env` file should look like this (with your values filled in):

```
CHANNEL_ID=107xxxxxxxxxxxxxxxx
DISCORD_TOKEN=MTAxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

- Start app: `python -m poetry run start_app`

## App structure
This app was started based on the template: https://github.com/cjolowicz/cookiecutter-hypermodern-python

The main files are `src/MPTbot/checker.py` and `src/MPTbot/bot.py

### `checker.py`

This file contains the core logic for checking the API server. The `MPTChecker` class has a `check` method which does the important stuff. Changes are detected against its record of shows in `self.shows`.

### `bot.py`

This file contains the logic for connecting to Discord. It instantiates an instance of the `MPTChecker` mentioned above. There is also a utility function `start_bot` which can bootstrap the entire bot process.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_MPTbot_ is free and open source software.

