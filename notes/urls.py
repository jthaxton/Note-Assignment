from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views


urlpatterns = [ 
    path('', index, name='index'),

]
