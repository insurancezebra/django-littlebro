import anyjson
from datetime import datetime
from time import time
from pymongo.connection import Connection
from littlebro.backends.base import BaseBackend
from littlebro.conf import settings

class MongoBackend(BaseBackend):
    """
    Saves tracking events to MongoDB.
    """
    def __init__(self, *args, **kwargs):
        # Somewhere in here: Test whether Mongo/PyMongo are installed
        BaseBackend.__init__(self, *args, **kwargs)
        self.host = settings.MONGODB_HOST
        self.port = settings.MONGODB_PORT
        self.collection = settings.DEFAULT_MONGO_COLLECTION
        self.db = settings.DEFAULT_MONGO_DB
        
    def _connect(self):
        return Connection(host=self.host, port=self.port)

    def _set_db(self, collection):
        self.db = collection
        return
    
    def _get_db(self):
        return self.db

    def _set_collection(self, collection):
        self.collection = collection
        return
    
    def _get_collection(self):
        conn = self._connect()
        return conn[self._get_db()][self.collection]
       
    def save(self, event, params, collection=None):
        "Save the event in MongoDB collection"
        if collection:
            self._set_collection(collection)
        col = self._get_collection()
        col.insert({
            'event': event,
            'timestamp': datetime.fromtimestamp(time()),
            'params': params
        })