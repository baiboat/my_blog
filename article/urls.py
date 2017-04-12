#!/usr/bin/env python
#-*- coding:utf-8 -*-
from . import views
from django.conf.urls import  url

urlpatterns = [
    url(r'^$', views.home, name='index'),
    url(r'^([0-9]+)/$',views.detail, name='detail'),
    url(r'^test/$',views.test, name='test'),

]