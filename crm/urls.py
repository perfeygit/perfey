from django.conf.urls import url
from crm import views
urlpatterns = [
    url(r'^index/$', views.index,name='index'),

]