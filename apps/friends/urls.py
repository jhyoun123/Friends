from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'add_home$', views.add_home),
    url(r'add/(?P<id>\d+)$', views.add),
    url(r'view$', views.view),
    url(r'delete/(?P<id>\d+)$', views.delete),
]