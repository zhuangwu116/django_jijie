"""django_jijie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from demo import views
from django.views.generic import TemplateView,RedirectView
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url(r'^publisher/$',views.publisher,name='publisher'),
    url(r'^forms/$',views.form,name='forms'),
    url(r'^zidingyifields/$', views.testlist, name='zidingyifields'),
    url(r'^tasks/$', views.ShowTasksView.as_view(), name='tasks'),
    url(r'^task/(?P<task_id>\d+)/$', views.DisplaySingleTaskView.as_view(), name='tasks'),
    url(r'^success',views.success,name='success'),
    url(r'^addtask',views.AddTaskView.as_view(),name='addtask'),
    url(r'^ajax',views.more_publisher,name='ajax'),
    url(r'^ajax',views.more_publisher,name='ajax'),
    url(r'^rest_framework/$',views.PublisherListView.as_view(),name='rest'),
    url(r'^rest_framework/(?P<pk>[0-9]+)$',views.publisher_detail,name='publisher_detail'),
    url(r'^signal/$',views.signal_view,name='signal'),
]
