from falcon_api_boilerplate.utils.config import get_config


def origin_is_authorized(origin: str):
    domains = get_config('cors')
    if origin in domains:
        return True
    return False
