===============================
Little Brother is watching ...
===============================

django-littlebro is a granular event tracking framework designed to be used in a
manner similar to Django's built-in cache system.

It works with Celery and MongoDB to provide quick, asynchronous event tracking.

The project is a fork of HonzaKrai's django-event-tracker:
https://github.com/ella/django-event-tracker

Requirements
============

I just started working on this project, so an installation package is forthcoming.
In the mean time:

 * Install django-littlebro into your environment
 * Install and configure celery, django-celery, carrot, pymongo and a message broker like RabbitMQ or ghettoq
 * add ``littlebro.apps.events`` to your ``INSTALLED_APPS`` and syncdb
 * customize your settings, see ``littlebro.conf.defaults`` for complete list of
   options and their default values

.. _`configure celery`: http://celeryproject.org/introduction.html#configuring-your-django-project-to-use-celery

Usage
=====

For now, only granular view-level tracking is enabled. To invoke it, simply import
the tracker:

from littlebro import tracker

And then use its track_event method to record events:

tracker.track_event('event-name', {'extra': 'parameters', 'go': 'here'})

Use the 'dummy' tracker and 'simple' backend to save tracked events synchronously to
the database. Use the 'celery' tracker and 'mongo' to enable asynchronous processing
with celery. Note that you'll have to be running celeryd and celerybeat daemons for
that to work.

Note
====

This was written on Dec. 9, 20111, after only two days of work on the project. Still
a lot of work to do, but we should have a totall functional, easy to install package
up in a week or so.

