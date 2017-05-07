# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from demo.models import *
# Create your views here.
from .forms import *
def index(request):

    return render(request,'index.html',{'tmpValue':[1,2,3]})
def form(request):
    forms=AddForm()
    return render(request,'form.html',{'form':forms})
def publisher(request):
    return render(request,'publisher.html',{"showType":"所有的列表","publisherList":Publisher.publisherManager.cityqueryset()})