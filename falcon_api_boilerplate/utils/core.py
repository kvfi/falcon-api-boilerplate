import functools
import logging
import os
import uuid
from datetime import datetime
from typing import Union

import bcrypt

log = logging.getLogger(__name__)


def rgetattr(obj, attr):
    def _getattr(obj, attr):
        return obj.get(attr)

    return functools.reduce(_getattr, [obj] + attr.split('.')).replace('/', '\\')


def str_to_date(date: str, date_format: str) -> datetime.date:
    if date:
        return datetime.strptime(date, date_format).date()
    else:
        return None


def date_to_str(date: datetime.date, date_format: str) -> Union[str, None]:
    if date:
        return date.strftime(date_format)
    else:
        return None


def hash_password(psw):
    return bcrypt.hashpw(psw.encode('utf-8'), bcrypt.gensalt()).decode('utf8')


def check_password(psw, hashed):
    try:
        return bcrypt.checkpw(psw.encode(), hashed.encode())
    except Exception as e:
        log.exception(e)
        return False


def has_params(data, params):
    params = set(params)
    return params.issubset(data.keys())


def get_file_path_info(path: str):
    base = os.path.basename(path)
    return os.path.splitext(base)


def generate_uuid():
    return str(uuid.uuid4())
