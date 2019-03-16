from django.contrib import admin

# Register your models here.

# -*- coding: utf-8 -*-

from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sim.models import *
from django.apps import apps

for model in apps.get_app_config('sim').models.values():
    admin.site.register(model)
