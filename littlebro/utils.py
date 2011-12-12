import importlib
from littlebro.conf import settings

def _get_backend_cls():
    try:
        backend = 'littlebro.backends.%s' % BACKEND_CLASSES[settings.DB_BACKEND]
        mod_path, cls_name = backend.rsplit('.', 1)
        mod = importlib.import_module(mod_path)
        backend_cls = getattr(mod, cls_name)
    except (AttributeError, ImportError, ValueError, KeyError), e:
        raise InvalidBackendError(
            'Could not find a backend named %s' %  e)
    return backend_cls()