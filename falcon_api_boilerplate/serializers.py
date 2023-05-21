import yaml


def error_serializer(req, resp, exception):
    preferred = req.client_prefers(('application/x-yaml',
                                    'application/json'))

    if preferred is not None:
        if preferred == 'application/json':
            representation = exception.to_json()
        else:
            representation = yaml.dump(exception.to_dict(), encoding=None)

        resp.body = representation
        resp.content_type = preferred
