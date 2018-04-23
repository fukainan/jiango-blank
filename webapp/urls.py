# -*- coding: utf-8 -*-
# Created on 2015-8-26
# @author: Yefei
# @version: $Id:$
from webapp import settings
from django.conf.urls import include, url
from jiango.admin.loader import admin_urls
#from jiango.api.loader import api_urls
#from jiango.cms.urls import urlpatterns as cms_urls

from webapp import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^admin/', admin_urls()),
#    url(r'^api/captcha/', include('jiango.captcha.urls')),
#    url(r'^api/', api_urls()),
#    *cms_urls,
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.PUBLIC_URL, document_root=settings.PUBLIC_ROOT)
