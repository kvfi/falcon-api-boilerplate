from pathlib import Path

import yaml

DEFAULT_SETTINGS = {
    'TEMPLATES_DIR': 'templates'
}


def app_config():
    with open(Path.cwd().joinpath('config.yml')) as f:
        config = yaml.load(f.read(), Loader=yaml.FullLoader)
    return config


app_config = app_config()
