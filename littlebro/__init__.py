VERSION = (0, 2, 0)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

TRACKER_CLASSES = {
    'dummy': 'dummy.DummyTracker',
    'celery': 'celery.CeleryTracker'
}

BACKEND_CLASSES = {
    'simple': 'simple.SimpleBackend',
    'mongo': 'mongo.MongoBackend'
}