import functools
import logging
from typing import Any

from falcon_api_boilerplate.settings import app_config

log = logging.getLogger(__name__)


def rgetattr(obj, attr):
    def _getattr(obj, attr):
        return obj.get(attr)

    return functools.reduce(_getattr, [obj] + attr.split('.'))


def get_config(name: str, default: str = None) -> Any:
    # TODO: force app to return non-zero in case config is critical
    try:
        return rgetattr(app_config, name)
    except Exception as e:
        if default:
            log.error('Variable {} was not found. Defaulting to {}...'.format(name, default), e)
            return default
