# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from demo.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from demo.forms import *
from django.shortcuts import render
from .forms import SetCityForm
# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','country','state_province','city','website',)
    search_fields = ('name','city',)
    list_filter = ('state_province',)
    ordering = ('-id',)
    change_form_template = 'change_form.html'
    # exclude = ('name','address',)
    fieldsets = (
        (None, {
            'fields': ('name', 'address',)
        }),
        ('高级', {
            'classes': ('collapse',),
            'fields': ('city', 'state_province','country','website',),
        }),
    )

    def print_publisher(self, request, queryset):
        for qs in queryset:
            print(qs)

    def set_type_action(self, request, queryset):
        if request.POST.get('post'):
            form=SetCityForm(request.POST)
            if form.is_valid():
                city=form.cleaned_data['city']
            for qs in queryset:
                qs.city = city
                qs.save()
        else:
            return render(request,'set_city.html',
                    {'form':SetCityForm(initial={'_selected_action':request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
                     ,'objects':queryset})
        self.message_user(request,"%s pusher were changed with city 上海" % len(queryset))
    def get_actions(self, request):
        actions=super(PublisherAdmin,self).get_actions(request)
        if 'hello' in actions:
            del actions['hello']
        return actions
    set_type_action.short_description = 'just_test'
    actions = [print_publisher, set_type_action]
admin.site.unregister(User)
@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','is_staff')
    list_filter = ('is_staff',)
    search_fields = ('last_name',)
# admin.site.register(Publisher,PublisherAdmin)
class AddFormAdmin(admin.ModelAdmin):
    forms=AddForm
def say_hello(modeladmin,request,queryset):
    print('hello')
admin.site.register(FormEntry,AddFormAdmin)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)

admin.site.add_action(say_hello,'hello')
admin.site.disable_action('delete_selected')