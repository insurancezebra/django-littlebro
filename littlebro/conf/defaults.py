from django.conf import settings

# Tracking system backend. Options are 'dummy' and 'celery'
TRACKER_BACKEND = getattr(settings, 'LITTLEBRO_TRACKER_BACKEND', 'dummy')

# Database backend. Options are 'simple' and 'mongo'
DB_BACKEND = getattr(settings, 'LITTLEBRO_DB_BACKEND', 'simple')

# Settings for message routing in Celery
# More information here: http://ask.github.com/celery/userguide/routing.html
ROUTING_KEY = getattr(settings, 'LITTLEBRO_ROUTING_KEY', 'littlebro')
ROUTING_KEY = getattr(settings, 'LITTLEBRO_EXCHANGE', 'littlebro')
ROUTING_KEY = getattr(settings, 'LITTLEBRO_QUEUE', 'littlebro')

# Length of time between asynchronous updates to database, in seconds.
# Also known as the length of time between celerybeat cycles.
TASK_PERIOD = getattr(settings, 'LITTLEBRO_TASK_PERIOD', 3*60)

# Settings for MongoDB
MONGODB_HOST = getattr(settings, 'LITTLEBRO_MONGODB_HOST', 'localhost')
MONGODB_PORT = getattr(settings, 'LITTLEBRO_MONGODB_PORT', 27017)
DEFAULT_MONGO_DB = getattr(settings, 'LITTLEBRO_MONGODB_DB', 'littlebro')
DEFAULT_MONGO_COLLECTION = getattr(settings, 'LITTLEBRO_MONGODB_COLLECTION', 'littlebro')