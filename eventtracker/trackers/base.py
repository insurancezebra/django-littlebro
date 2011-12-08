from eventtracker.conf import settings

class InvalidTrackerError(Exception):
    pass

class BaseTracker(object):
    def __init__(self, *args, **kwargs):
        self.backend = settings.DB_BACKEND