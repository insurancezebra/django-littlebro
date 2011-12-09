import importlib
from datetime import timedelta
from celery.task import PeriodicTask
from celery.registry import tasks
from carrot.messaging import Consumer
from pymongo.connection import Connection
from littlebro.conf import settings
from littlebro.trackers.celery import _get_carrot_object, _close_carrot_object
from littlebro import BACKEND_CLASSES

def collect_events():
    """
    Collect all events waiting in the queue and store them in the database.
    """    
    consumer = None
    collection = None
    backend_cls = None

    try:
        backend = 'littlebro.backends.%s' % BACKEND_CLASSES[settings.DB_BACKEND]
        mod_path, cls_name = backend.rsplit('.', 1)
        mod = importlib.import_module(mod_path)
        backend_cls = getattr(mod, cls_name)
    except (AttributeError, ImportError, ValueError, KeyError), e:
        raise InvalidBackendError(
            'Could not find a backend named %s' %  e)
    
    try:
        consumer = _get_carrot_object(Consumer, queue=settings.QUEUE)
        connection = Connection(host=settings.MONGODB_HOST, port=settings.MONGODB_PORT)

        for message in consumer.iterqueue():
            e, t, p, c = message.decode()
            backend_cls().save(e, p, c)
            message.ack()

    finally:
        _close_carrot_object(consumer)
        if collection:
            try:
                collection.connection.close()
            except:
                pass

class ProcessEventsTask(PeriodicTask):
    "Celery periodic task that collects events from queue."
    run_every = timedelta(seconds=settings.TASK_PERIOD)

    def run(self, **kwargs):
        collect_events()

tasks.register(ProcessEventsTask)