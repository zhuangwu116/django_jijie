# -*- coding: utf-8 -*-
from django import forms
from .models import FormEntry
from django.core.validators import ValidationError
class SubInputText(forms.TextInput):
    class Media:
        css={
            'all': ('input.css',)
        }
class AddForm(forms.ModelForm):
    class Meta:
        model=FormEntry
        fields=['author','title']
        widgets={
            'author':forms.Textarea(attrs={'cols':'20','row':1}),
            'title':SubInputText(),
        }
    # def clean_author(self):
    #     print ('clean author')
    #     data=self.cleaned_data['author']
    #     if 'allen' not in data:
    #         raise ValidationError('no in allen')
    #     return data
    def clean(self):
        author=self.cleaned_data['author']
        title=self.cleaned_data['title']
        object=FormEntry.objects.filter(author=author,title=title)
        if object:
            raise ValidationError('no in allen')
class SetCityForm(forms.Form):
    city=forms.CharField()
    _selected_action=forms.CharField(widget=forms.MultipleHiddenInput)