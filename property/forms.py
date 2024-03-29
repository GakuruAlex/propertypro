from django import forms
from .models import House,Property
from accounts.models import Owner

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ("name","location")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Enter name of Property'})
        self.fields['location'].widget.attrs.update({'placeholder': 'Enter location of Property'})
       
class HouseForm(forms.ModelForm):
        class Meta:
            model = House
            fields = '__all__'