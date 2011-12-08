from django.conf.urls.defaults import *
from littlebro.apps.events import views

urlpatterns = patterns('',
    url(r'^(?P<event>[\w-]+)/$', views.track_event, name='littlebro-track-event'),
)