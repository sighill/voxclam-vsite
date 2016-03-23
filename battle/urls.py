from django.conf.urls import url

from . import views

# all URLs here start with /battle/
urlpatterns = [
	url(r'^select/', views.battleSelect), # for URL /battle/select
    url(r'^execute/(?P<GIDA>\d+)/(?P<GIDB>\d+)/$', views.battleExecute), # for URL /battle/execute/PIDA/PIDB
]
