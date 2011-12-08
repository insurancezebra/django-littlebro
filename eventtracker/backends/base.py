from eventtracker.conf import settings

class InvalidBackendError(Exception):
    pass

class BaseBackend(object):
    def __init__(self, *args, **kwargs):
        self.host = None
        self.port = None
        self.collection = None
        self.db = None