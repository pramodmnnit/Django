from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
	url(r'^$', "posts.views.list"),
    url(r'^create/$', "posts.views.create"),
    url(r'^(?P<id>\d+)/$', "posts.views.detail",name='detail'),
    url(r'^(?P<id>\d+)/update/$', "posts.views.update"),
    url(r'^delete/$', "posts.views.delete"),
]