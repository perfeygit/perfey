from django.conf.urls import url
from media import views
urlpatterns = [
    url(r'^video/(?P<id>\d+)$', views.video,name='video'),

]