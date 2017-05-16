# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from demo.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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
admin.site.unregister(User)
@admin.register(User)
class MyUserAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','is_staff')
    list_filter = ('is_staff',)
    search_fields = ('last_name',)
# admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)
