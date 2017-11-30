from django.conf.urls import url

from . import views

app_name = 'todo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^savetodo/$', views.savetodo, name='savetodo'),
    url(r'^completetodo/$', views.completetodo, name='completetodo')
]


