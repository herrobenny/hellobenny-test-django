from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from blogapp import views

urlpatterns = patterns('',
    url(r'^hello_world/$', views.hello_world)
)