import os

from jinja2 import Environment, FileSystemLoader

from falcon_api_boilerplate.settings import DEFAULT_SETTINGS
from falcon_api_boilerplate.utils.config import get_config

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), get_config('templates.dir', DEFAULT_SETTINGS['TEMPLATES_DIR']))

tpl_env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, autoescape=True)
