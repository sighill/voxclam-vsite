from django.contrib import admin
from django.contrib.gis import admin
from .models import Sestieri


admin.site.register(Sestieri, admin.GeoModelAdmin)