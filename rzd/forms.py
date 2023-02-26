from django.forms import ModelForm, TextInput, NumberInput

#ModelForm для наследования
#TextInput для описания поля ввода текста

from .models import Road
from .models import Region
from .models import Station

class RoadForm(ModelForm):
    class Meta:
        model = Road
        fields = ['name', 'short_name', 'kod']
        widgets = {
          "name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Название дороги', }),
          "short_name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Краткое название дороги', }),
          "kod":  NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Код дороги', }),
        }


class RegionForm(ModelForm):
    class Meta:
        model = Region
        fields = ['name', 'kod', 'road']
#        widgets = {
#          "name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Название региона', }),
#          "kod":  NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Код региона', }),
##          "road":  FieldInput(attrs={ 'class': 'form-control', 'placeholder': 'Код региона', }),
#        }


class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'kod', 'region', 'rvc', 'csvt']
#        widgets = {
#          "name": TextInput(attrs={ 'class': 'form-control', 'placeholder': 'Название региона', }),
#          "kod":  NumberInput(attrs={ 'class': 'form-control', 'placeholder': 'Код региона', }),
##          "road":  FieldInput(attrs={ 'class': 'form-control', 'placeholder': 'Код региона', }),
#        }
