

from django.conf.urls import url

from . import views

app_name = 'accounts'
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^createuser/$', views.createuser, name='createuser'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.loginpage, name='login'),
    url(r'^loginuser/$', views.loginuser, name='loginuser'),
    url(r'^logout/$', views.logoutuser, name='logout')
]

