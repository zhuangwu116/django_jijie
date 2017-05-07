# -*- coding: utf-8 -*-
from django.db import models
import ast
class ListFiled(models.TextField):
    description = 'just a listfiled'
    def __init__(self,*args,**kwargs):
        super(ListFiled,self).__init__(*args,**kwargs)
    def from_db_value(self, value, expression, connection, context):
        print ('from_db_value')
        if not value:
            value=[]
        if isinstance(value,list):
            return value
        print ('value type',type(value))
        return ast.literal_eval(value)
    def get_prep_value(self, value):
        print ('get_prep_value')
        if not value:
            return value
        print('value type',type(value))
        return str(value)
