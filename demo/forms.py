from django import forms
class AddForm(forms.Form):
    author=forms.CharField(label='the author',min_length=1,max_length=10)
    title=forms.CharField()
