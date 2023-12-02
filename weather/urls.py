__author__ = 'Saheed'
__date__ = '28/07/2018'

from django.conf.urls import url
from . import views

#This is the weather URL
urlpatterns = [
    url('', views.index, name='index'),
]