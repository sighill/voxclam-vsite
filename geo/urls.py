from django.conf.urls import url, include
from django.contrib.gis import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mapclemence/', views.mapClemence),
]