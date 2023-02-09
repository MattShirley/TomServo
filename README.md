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

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_MPTbot_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/MattShirley/MPTbot/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/MattShirley/MPTbot/blob/main/LICENSE
[contributor guide]: https://github.com/MattShirley/MPTbot/blob/main/CONTRIBUTING.md
[command-line reference]: https://MPTbot.readthedocs.io/en/latest/usage.html
