from django import forms
from .models import FormEntry
class AddForm(forms.ModelForm):
    class Meta:
        model=FormEntry
        fields=['author','title']

