from time import time
from django.utils import importlib
from littlebro.trackers.base import BaseTracker
from littlebro.utils import _get_backend_cls
from celery.task import task


class CeleryNewTracker(BaseTracker):
    """
    Saves tracking events asynchronously into either a regular or Mongo DB table using Celery/Kombu.
    """
    def __init__(self, *args, **kwargs):
        BaseTracker.__init__(self, *args, **kwargs)
        
    def track_event(self, event, params={}, collection=None):
        self._track_event.delay(self, event, time(), params, collection)

    @task
    def _track_event(self, event, time=time(), params={}, collection=None):
        backend = _get_backend_cls()
        backend.save(event, time, params, collection)