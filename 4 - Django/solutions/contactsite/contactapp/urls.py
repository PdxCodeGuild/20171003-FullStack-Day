
from django.conf.urls import url

from . import views

app_name = 'contactapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^savecontact/$', views.savecontact, name='savecontact')
]


