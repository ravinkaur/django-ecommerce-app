from django.conf.urls import patterns, url

from apps.appointment import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)