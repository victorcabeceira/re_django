from django.conf.urls import url, include
from re_django.core import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]
