import importlib
from littlebro.conf import settings
from littlebro.trackers.base import InvalidTrackerError

VERSION = (0, 0, 2)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

TRACKER_CLASSES = {
    'dummy': 'dummy.DummyTracker',
    'celery': 'celery.CeleryTracker'
}

BACKEND_CLASSES = {
    'dummy': 'dummy.DummyBackend',
    'mongo': 'mongo.MongoBackend'
}

def get_tracker(backend=settings.TRACKER_BACKEND, **kwargs):
    try:
        backend = 'littlebro.trackers.%s' % TRACKER_CLASSES[backend]
        mod_path, cls_name = backend.rsplit('.', 1)
        mod = importlib.import_module(mod_path)
        backend_cls = getattr(mod, cls_name)
    except (AttributeError, ImportError, ValueError) ,e:
        raise InvalidTrackerError(
            'Could not find a tracker named %s: %s' % (backend, e))
    return backend_cls()

tracker = get_tracker()