# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from demo.models import *
from django.views.generic import TemplateView,ListView
# Create your views here.
from .forms import *
def index(request):

    return render(request,'index.html',{'tmpValue':[1,2,3]})
def form(request):
    if request.method=='POST':
        forms=AddForm(request.POST)
        if not forms.is_valid():
            forms = AddForm()
            print 'invalid'
            return render(request, 'form.html', {'form': forms})
        author=forms.cleaned_data['author']
        title=forms.cleaned_data['title']
        print author,title
    forms=AddForm()
    return render(request,'form.html',{'form':forms})
def testlist(request):
    test=ListTest()
    test.labels=["python","django"]
    test.labels.append('allen')
    test.save()
    return HttpResponse('success')

class ShowTasksView(ListView):
    template_name = 'task.html'
    model = Publisher
def publisher(request):
    return render(request,'publisher.html',{"showType":"所有的列表","publisherList":Publisher.publisherManager.cityqueryset()})