import random
import string

from falcon.http_error import HTTPError


class HttpError(HTTPError):
    """Represents a generic HTTP error.
    """

    def __init__(self, status, path: str, error: list = []):
        super(HttpError, self).__init__(status)
        self.status = status
        self.path = path
        self.error = error

    def to_dict(self, obj_type=dict):
        """Returns a basic dictionary representing the error.
        """
        super(HttpError, self).to_dict(obj_type)
        obj = {
            'status': int(self.status[0:3]),
            'path': self.path,
            'error': self.error,
            'trace_id': ''.join(random.choices(string.ascii_letters, k=15))
        }

        return obj
