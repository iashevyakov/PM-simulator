from django.conf.urls import url

from sim.views import *

app_name = "sim"

urlpatterns = [
    url(r'^base$', base, name="base"),
    url(r'^question/(?P<q_id>[0-9]+)$', question, name='question'),
    url(r'^ajax_save$', ajax_save, name='ajax_save'),
    url(r'^results$', results, name='results')
]
