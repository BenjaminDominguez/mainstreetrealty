from django import forms
from .models import NewLead

class CMAForm(forms.ModelForm):
    class Meta:
        model = NewLead
        fields = [
        'name','sq_ft','move_in_date','beds','baths','email','phone','property_type',
        'address','move_in_date','preffered_method_of_contact','description'
        ]

    #this model form has a save() method

class IndexForm(forms.Form):
    email = forms.EmailField()
