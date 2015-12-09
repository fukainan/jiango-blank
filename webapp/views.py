# -*- coding: utf-8 -*-
# Created on 2015-8-31
# @author: Yefei
# @version: $Id:$
from jiango.shortcuts import renderer


render = renderer()


@render
def index(request, response):
    return locals()
