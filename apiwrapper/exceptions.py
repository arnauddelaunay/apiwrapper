from flask import jsonify


class WrapperError(Exception):
    status_code = 400
    message = "No model loaded yet. Run api.load_model(model) before launching the api"

    def __init__(self, message=message, status_code=status_code, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv
