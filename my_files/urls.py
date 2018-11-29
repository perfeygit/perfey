from django.conf.urls import url
from my_files import views
urlpatterns = [
    url(r'^files/(?P<down_file>.*)', views.files,name='files'),
]