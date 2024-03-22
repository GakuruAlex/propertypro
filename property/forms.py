from django import forms
from .models import House
from accounts.models import Owner
class PropertyForm(forms.Form):
    name = forms.CharField(max_length=25, required=False)
    location = forms.CharField( max_length=25, required=True)
    no_houses = forms.IntegerField( required=True)
    houses = forms.ModelChoiceField(queryset=House.objects.all())
    owner =forms.ModelMultipleChoiceField(queryset=Owner.objects.all())
