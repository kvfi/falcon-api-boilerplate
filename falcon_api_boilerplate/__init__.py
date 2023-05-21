import logging.config
import sys
import warnings
from pathlib import Path

import falcon
import yaml
from falcon_multipart.middleware import MultipartMiddleware
from waitress import serve

from falcon_api_boilerplate.config import Config
from falcon_api_boilerplate.db import session
from falcon_api_boilerplate.middlewares import SQLAlchemySessionManagerMiddleware, CORSMiddleware, \
    RequestLoggerMiddleware, AuthMiddleware
from falcon_api_boilerplate.serializers import error_serializer
from falcon_api_boilerplate.utils.config import get_config

if not sys.warnoptions:
    warnings.simplefilter('ignore')

with open(Path.cwd().joinpath('logging.yml'), 'r') as stream:
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)

log = logging.getLogger(__name__)

api = falcon.App(
    middleware=[
        RequestLoggerMiddleware(),
        SQLAlchemySessionManagerMiddleware(session),
        AuthMiddleware(),
        CORSMiddleware(),
        MultipartMiddleware()]
)

api.set_error_serializer(error_serializer)

log.info('Application "{}" initialized.'.format(get_config('app.name')))

if __name__ == "__main__":
    serve(api, host='localhost', port=8041)
