# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from demo2.models import *
# Create your views here.
def student(request):
    st=Student.objects.all()
    return render(request,'student.html',locals())

