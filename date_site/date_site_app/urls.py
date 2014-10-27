from django.conf.urls import patterns,url
from date_site_app import views

urlpatterns=patterns('',
    url(r'^$',views.index,name='index'),
                        
)