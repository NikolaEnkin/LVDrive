from django import forms
from cars.models import Car, CarImage


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner', 'approved']

        labels = {
            'make': 'Make',
            'model_name': 'Model Name',
            'horse_power': 'Horse Power',
            'year': 'Year of Manufacture',
            'price_per_hour': 'Price per Hour (EUR)',
            'engine_size': 'Engine Size (cc)',
            'body_type': 'Body Type',
            'fuel_type': 'Fuel Type',
            'features': 'Optional Features',
            'image': 'Car Image',
        }

        widgets = {
            'make': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Mercedes'
                }
            ),
            'model_name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. W222'
                }
            ),
            'horse_power': forms.NumberInput(
                attrs={
                    'min': 0, 'placeholder': 'e.g. 300'
                }
            ),
            'year': forms.DateInput(
                attrs={'type': 'date'
                       }
            ),
            'price_per_hour': forms.NumberInput(
                attrs={
                    'min': 0, 'step': '0.01'
                }
            ),
            'engine_size': forms.NumberInput(
                attrs={
                    'placeholder': 'Minimum 900 cc'
                }
            ),

        }

class CreateCarForm(BaseCarForm):
    ...

class EditCarForm(BaseCarForm):
    ...

class DeleteCarForm(BaseCarForm):
    ...

class SearchForm(forms.Form):
    query = forms.CharField(
        label='',
        required=False,
        max_length=70,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Search for a car...',
                'class': 'search-input'
            }
        )
    )