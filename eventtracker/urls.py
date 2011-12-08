from django.conf.urls.defaults import *
from eventtracker.apps.events import views

urlpatterns = patterns('',
    url(r'^(?P<event>[\w-]+)/$', views.track_event, name='eventtracker-track-event'),
)