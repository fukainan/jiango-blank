# -*- coding: utf-8 -*-
# Created on 2015-4-2
# @author: Yefei
# @version: $Id:$
from django.conf import settings
from webapp import config as C


def config(request):
    return {'SETTINGS':settings, 'CONFIG':C}
