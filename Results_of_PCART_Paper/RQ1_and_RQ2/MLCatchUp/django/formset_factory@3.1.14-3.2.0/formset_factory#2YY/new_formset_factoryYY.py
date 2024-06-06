from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
from django.forms import formset_factory
ExampleFormSet = formset_factory(form=ExampleForm, absolute_max=None, can_delete_extra=True)
