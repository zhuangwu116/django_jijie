from django import forms
from .models import FormEntry
from django.core.validators import ValidationError
class AddForm(forms.ModelForm):
    class Meta:
        model=FormEntry
        fields=['author','title']
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
