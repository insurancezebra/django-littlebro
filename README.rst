===============================
Little Brother is watching ...
===============================

django-littlebro is a granular event tracking framework designed to be used in a
manner similar to Django's built-in cache system.

It works with Celery and MongoDB to provide quick, asynchronous event tracking.

The project is a fork of HonzaKral's django-event-tracker:
https://github.com/ella/django-event-tracker

Requirements
============

Littlebro will work synchronously out of the box, simply do this:

 * pip install django-littlebro
 * add ``littlebro` to your ``INSTALLED_APPS`` and syncdb
 * customize your settings, see ``littlebro.conf.defaults`` for complete list of
   options and their default values

If you want to enable asynchronous tracking using celery, you'll need to follow a few more steps:

 * add djkombu, ghettoq and djcelery to INSTALLED_APPS. You can also use RabbitMQ instead of ghettoq for better performance.
 * Set up a few Celery settings in your settings.py. A simple configuration might look like this:

     - CARROT_BACKEND = "ghettoq.taproot.Database"
     - CELERY_IMPORTS = ('littlebro.tasks',)
     - BROKER_BACKEND = "django"

 * You'll also need to add the standard django-celery setup line in your settings.py as well:

     - import djcelery
     - djcelery.setup_loader()

 * If you're running celery in production, you'll need to daemonize it. We like to use supervisor for that. Great instructions are available here: http://ericholscher.com/blog/2010/nov/2/celery-tips/
 * And if you're using mod_wsgi, you'll need to add this setting to your django wsgi file: os.environ["CELERY_LOADER"] = "django"

Finally, if you want to use MongoDB, you'll have to install that as well.

Yeah, it's a lot of work. Look for this install process to be simplified in future versions.


Usage
=====

Three kinds of tracking are currently available: middleware, view-level, or granular
within views.

Middleware will track every request running through your app. There's really no reason
to use it if you're using Google Analytics or another tracking system, but on the off
chance you want to go that route, just insert:

**littlebro.middleware.TrackerMiddleware**

Into your MIDDLEWARE_CLASSES setting.

If you want to track activity at the view level, you can use the track_event decorator
on top of any view in your app:

**@track_event('event-name-here')**
**def this_is_a_view(request):**

And finally if you want to track activity within a view, you can take advantage of
littlebro's granular event tracking as well:

**from littlebro import tracker**

And then use its track_event method to record events:

**tracker.track_event('event-name', params={'extra': 'parameters', 'go': 'here'})**

Use the 'dummy' tracker and 'simple' backend to save tracked events synchronously to
the database. Use the 'celery' tracker and 'mongo' to enable asynchronous processing
with celery. Note that you'll have to be running celeryd and celerybeat daemons for
that to work.