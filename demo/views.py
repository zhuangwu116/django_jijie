# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse,Http404
from demo.models import *
from django.views.generic import TemplateView,ListView,View
# Create your views here.
from .forms import *
def success(request):
    return render(request,'success.html',locals())
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
    context_object_name = 'my_favorite_publishers'
class DisplaySingleTaskView(TemplateView):
    template_name = 'single_task.html'
    context_object_name='task'
    def get_context_data(self, **kwargs):
        context=super(DisplaySingleTaskView,self).get_context_data(**kwargs)
        task_id=self.kwargs.get("task_id",0)
        context['task']=Publisher.publisherLists.get(id=task_id)
        return context
class AddTaskView(View):
    def get(self,request):
        return render(request,'add_task.html',{'form':AddForm})
    def post(self,request):
        form=AddTaskForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('success'))
def publisher(request):
    return render(request,'publisher.html',{"showType":"所有的列表","publisherList":Publisher.publisherManager.cityqueryset()})

def more_publisher(request):
    if request.is_ajax():
        objects=Publisher.publisherLists.all()
        data=get_json_objects(objects,Publisher)
        return HttpResponse(data,content_type='application/json')
    else:
        return render(request, 'ajax.html', {})

def json_filed(field_data):
    if isinstance(field_data,str):
        return "\""+field_data+"\""
    if isinstance(field_data,bool):
        if field_data=='False':
            return 'false'
        else:
            return 'true'
    return str(field_data)
def json_encode_dict(dict_data):
    json_data = "{"
    for (k,v) in dict_data.items():
        json_data=json_data+json_filed(k)+": "+json_filed(v)+", "
    json_data=json_data[:-2]+"}"
    return json_data

def json_encode_list(list_data):
    json_res="["
    for item in list_data:
        json_res=json_res+json_encode_dict(item)+", "
    return json_res[:-2]+"]"
def get_json_objects(objects,model_meta):
    concrete_model=Publisher._meta.concrete_model
    list_data=[]
    for obj in objects:
        dict_data={}
        for field in concrete_model._meta.local_fields:
            if field.name=='id':
                continue
            value=field.value_from_object(obj)
            dict_data[field.name]=value
        list_data.append(dict_data)
    data=json_encode_list(list_data)
    return data