


from django.conf.urls import url

from . import views

app_name = 'todoajax'
urlpatterns = [
    url(r'^$', views.index, name='gettodos'),
    url(r'^gettodos/$', views.gettodos, name='gettodos'),
    url(r'^savetodo', views.savetodo, name='savetodo')
]


