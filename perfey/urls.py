"""perfey URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from index import views
from django.conf import settings

from DjangoUeditor import urls as djud_urls

from chat import views as chatView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.redir_index),
    url(r'^index/', include('index.urls', namespace='index')),
    url(r'^crm/', include('crm.urls', namespace='crm')),
    url(r'^media/', include('media.urls', namespace='media')),

    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^my_files/', include('my_files.urls', namespace='my_files')),
    url(r'^live/', include('live.urls', namespace='live')),
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^ueditor/', include(djud_urls)),
]

# blog
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)