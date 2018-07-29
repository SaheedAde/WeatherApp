__author__ = 'Saheed'
__date__ = '28/07/2018'


from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs={'class' : 'input',
                                      'placeholder' : 'City Name'})
        }