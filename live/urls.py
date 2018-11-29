from django.conf.urls import url
from live import views
urlpatterns = [
    url(r'^index/', views.index,name='index'),
]