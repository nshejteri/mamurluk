from django.conf.urls import patterns,url
from date_site_app import views

urlpatterns=patterns('',
    url(r'^$', views.index, name='index'), 
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),                       
)