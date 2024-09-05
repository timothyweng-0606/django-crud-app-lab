from django import forms
from .models import Vaccine

class VaccineForm(forms.ModelForm):
    class Meta:
        model = Vaccine
        fields = ['date', 'vaccine']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }