from django import forms
from .models import MyModel

class MyModelForm(forms.Form):
    my_model = forms.ModelChoiceField(queryset=MyModel.objects.all(), label='Select User')
