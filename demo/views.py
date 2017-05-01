# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from demo.models import *
# Create your views here.
def index(request):

    return render(request,'index.html',{'tmpValue':[1,2,3]})
def publisher(request):
    return render(request,'publisher.html',{"showType":"所有的列表","publisherList":Publisher.publisherManager.cityqueryset()})