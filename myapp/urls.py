from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/?$', views.index, name='index'),
    url("explain", views.explain, name='explain'),
]
