from django.conf.urls import include, url
from django.contrib import admin
from login.views import *
import user_profile

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name' : 'login/login.html'}),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name' : 'login/login.html'}),
    url(r'^logout/$', logout_page),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    url(r'^profile/', include('user_profile.urls')),
    url(r'^search/', user_profile.views.searchUsers),
]
