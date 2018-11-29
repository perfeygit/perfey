from django.conf.urls import url
from chat import views
urlpatterns = [
    url(r'^ws/(?P<user>.*)', views.ws, name='ws'),
    url(r'^index/', views.index, name='index'),
]