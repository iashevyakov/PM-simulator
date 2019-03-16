from django.conf.urls import url

from sim.views import *

app_name = "sim"

urlpatterns = [
    url(r'^base$', ba, name="base"),
    url(r'^question/(?P<q_id>[0-9]+)$', base, name='question')
]
