

from django.conf.urls import url

from . import views

app_name = 'quotes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^savequote/$', views.savequote, name='savequote')
]
