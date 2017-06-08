# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('gnosisdb.restapi.urls', namespace='api'))
]

admin.autodiscover()