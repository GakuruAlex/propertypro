from django.forms import forms
from .models import House
from accounts.models import Owner
class PropertyForm(forms.Forms):
    name = forms.CharField( max_length=25, required=True)
    location = forms.CharField( max_length=25, required=True)
    no_houses = forms.IntegerField( required=True)
    houses = forms.Foreignkey(House.house_number)
    owner =forms.ManyToManyField(Owner.name)
