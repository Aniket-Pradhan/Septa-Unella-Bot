# Septa-Unella-Bot

## How to setup?

1. First create a `secrets.yaml` file at the root of this project. The file should contain all the user secrets of the bot. An example `secrets.yaml` is uploaded as the `secrets-example.yaml`.
2. Next step is to create a list of users to shame. For that, create the `mod_list.yaml` file at the project root. Similarly, an example `mod_list.yaml` is present as `mod_list-example.yaml`.
3. Create a virtual environment (recommended but optional) for Python 3+. You can do this using: `python3 -m virtualenv ./.venv`. Then activate the virtual env.
4. Install the dependencies from `requirements.txt`.
5. Run main.py in `scripts/` directory: `python scripts/main.py`
6. Et voila!
