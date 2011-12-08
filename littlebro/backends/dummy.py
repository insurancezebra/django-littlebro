import anyjson
from littlebro.backends.base import BaseBackend
from littlebro.apps.events.models import Event

class DummyBackend(BaseBackend):
    def save(self, event, params, collection=None):
        Event.objects.create(event=event, params=anyjson.serialize(params))