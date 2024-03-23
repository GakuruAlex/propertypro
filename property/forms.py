from django import forms
from .models import House,Property
from accounts.models import Owner

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ("name","location","no_houses")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter name of Property'})
        self.fields['location'].widget.attrs.update({'placeholder': 'Enter location of Property'})
        self.fields['no_houses'].widget.attrs.update({'placeholder': 'Enter number of houses'})
