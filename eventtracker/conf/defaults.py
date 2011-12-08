from django.conf import settings

# Set backends for both tracker and database
TRACKER_BACKEND = 'dummy' # Options are 'dummy' and 'celery'
DB_BACKEND = 'mongo' # Options are 'dummy' and 'mongo'

# Settings for message routing in Celery
# More information here: http://ask.github.com/celery/userguide/routing.html
ROUTING_KEY = 'events'
EXCHANGE = 'events'
QUEUE = 'events'

# Length of time between asynchronous updates to database, in seconds.
# Also known as the length of time between celerybeat cycles.
TASK_PERIOD = 3*60

# Settings for MongoDB
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DEFAULT_MONGO_DB = 'events'
DEFAULT_MONGO_COLLECTION = 'events'