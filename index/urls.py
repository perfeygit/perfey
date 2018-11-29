from django.conf.urls import url
from index import views
urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^login/$', views.login,name='login'),
    url(r'^reg/$', views.reg,name='reg'),
    url(r'^logout/$', views.logout,name='logout'),
]