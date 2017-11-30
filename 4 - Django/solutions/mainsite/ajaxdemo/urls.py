from django.conf.urls import url

from . import views

app_name = 'ajaxdemo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^getdata/$', views.getdata, name='getdata'),
    url(r'^postdata/$', views.postdata, name='postdata')
]