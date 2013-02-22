from distutils.core import setup
import littlebro
import sys

VERSION = (0, 2, 1)
__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

REQUIRES = [
        'anyjson',
        'carrot>=0.6.0',
        'celery>=0.8.0',
        'pymongo',
        'django-celery',
        'django-kombu',
    ]

if sys.version_info < (2, 7):
    REQUIRES.insert(0, 'importlib')

setup(
    name = 'django-littlebro',
    version = __versionstr__,
    description = 'Django LittleBro: Asynchronous event tracking using MongoDB and Celery.',
    long_description = '\n'.join((
        'Django LittleBro',
        '',
        'Simple django application for asynchronous tracking of events',
        'Uses celery for transport of messages and MongoDB for event store.',
        'Forked from http://github.com/ella/django-event-tracker',
    )),
    author = 'Chase Davis',
    author_email='chase.davis@gmail.com',
    license = 'BSD',
    url='https://github.com/cirlabs',
    packages = ['littlebro', 'littlebro.conf', 'littlebro.trackers', 'littlebro.backends'],
    install_requires = REQUIRES
)