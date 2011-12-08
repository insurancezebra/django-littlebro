import anyjson
from eventtracker.backends.base import BaseBackend
from eventtracker.apps.events.models import Event

class DummyBackend(BaseBackend):
    def save(self, event, params, collection=None):
        Event.objects.create(event=event, params=anyjson.serialize(params))