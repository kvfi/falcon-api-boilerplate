import logging
from datetime import datetime

import jwt
from falcon import HTTPUnauthorized

from falcon_api_boilerplate.utils.config import get_config
from falcon_api_boilerplate.utils import jwt
from falcon_api_boilerplate.utils.security import origin_is_authorized

log = logging.getLogger(__name__)


class AuthMiddleware:

    def __init__(self):
        self.error = {}
        self.payload = {}
        self.exempt_endpoints = get_config('security.auth.exempt-endpoints')
        self.current_user_id = None

    def process_resource(self, req, _, resource, __):
        if req.path in self.exempt_endpoints or req.method == 'OPTIONS':
            return
        resource.current_user_id = jwt.get_jwt_payload(req.auth, 'id')

    def process_request(self, req, _):
        if req.path not in self.exempt_endpoints and req.method != 'OPTIONS':
            log.debug('Handling protected route: {}'.format(req.path))
            token = req.get_header('Authorization')

            if token is None:
                log.error('No token provided.')
                description = 'Please provide a token as part of the request.'
                raise HTTPUnauthorized('Authentication required.', description)

            jwt_is_valid, error = jwt.is_valid(token)
            if not jwt_is_valid:
                raise HTTPUnauthorized('Authentication could not be validated', error.value)


class CORSMiddleware(object):

    def process_request(self, req, resp):
        # log.debug('Request headers: {}'.format(req.headers))
        origin = req.get_header('ORIGIN')
        if origin and origin_is_authorized(origin):
            resp.set_header('Access-Control-Allow-Origin', origin)
            resp.set_header('Access-Control-Allow-Credentials', 'true')
            resp.set_header('Access-Control-Allow-Methods', 'GET, POST, HEAD, PUT, PATCH, DELETE')
            resp.set_header('Access-Control-Allow-Headers',
                            'Content-Type, Authorization, Accept, X-Requested-With, X-Auth-Provider')
            resp.set_header('Content-Type', 'application/json')


class SafeCache(object):

    def process_response(self, req, resp, resource, req_succeeded):
        # Control the cache in case the response contains an access token

        if 'access_token' in resp.media:
            resp.set_header('Cache-Control', 'no-store')
            resp.set_header('Pragma', 'no-cache')


class SQLAlchemySessionManagerMiddleware:
    """
    Create a session for every request and close it when the request ends.
    """

    def __init__(self, session):
        self.session = session

    def process_resource(self, req, resp, resource, params):
        if req.method == 'OPTIONS':
            return
        resource.session = self.session
        req.context['session'] = self.session()

    def process_response(self, req, resp, resource, req_succeeded):
        if req.method == 'OPTIONS':
            return

        if req.context.get('session'):
            if not req_succeeded:
                req.context['session'].rollback()
            req.context['session'].close()


class RequestLoggerMiddleware(object):

    def process_request(self, req, resp):
        if req.method == 'OPTIONS':
            return
        line = {
            'date': datetime.now().strftime('%m/%d/%y %H:%M:%S'),
            'verb': req.method,
            'path': req.relative_uri,
            'remote_ip': req.remote_addr
        }
        log.debug('Request: {}'.format(line))
