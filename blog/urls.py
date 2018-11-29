from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^post/(?P<id>\d+)/$', views.Detail, name="blog_detail"),
    url(r'^home/', views.home, name="blog_home"),
    url(r'^test/', views.Test, name="blog_test"),
    url(r'^add/', views.add, name="blog_add"),
    url(r'^del/(?P<id>\d+)/', views.delete, name="blog_del"),

]
