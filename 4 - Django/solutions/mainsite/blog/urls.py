

from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.viewposts, name='viewposts'),
    url(r'^viewpost/$', views.viewpost, name='viewpost'),
    url(r'^makepost/$', views.makepost, name='makepost'),
    url(r'^savepost/$', views.savepost, name='savepost'),
    url(r'^savecomment/$', views.savecomment, name='savecomment')
]




