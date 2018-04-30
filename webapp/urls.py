# -*- coding: utf-8 -*-
# Created on 2015-8-26
# @author: Yefei
# @version: $Id:$
from webapp import settings
from django.urls import path, include
from jiango.admin.loader import admin_urls
# from jiango.api.loader import api_urls
# from jiango.cms.urls import urlpatterns as cms_urls

from webapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin_urls()),
    # path('api/captcha/', include('jiango.captcha.urls')),
    # path('api/', api_urls()),
    # *cms_urls,
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.PUBLIC_URL, document_root=settings.PUBLIC_ROOT)
