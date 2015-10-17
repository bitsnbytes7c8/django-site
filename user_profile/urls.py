from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^create/$', views.create_profile),
    url(r'^view/$', views.view_profile),
    url(r'^edit/$', views.create_profile),
]
