# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from demo.models import *
# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','country','state_province','city','website',)
    search_fields = ('name','city',)
    list_filter = ('state_province',)
    ordering = ('-id',)
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

# admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Book)
