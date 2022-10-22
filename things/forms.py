"""Forms of the project."""

# Create your forms here.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


class ThingForm(forms.Form):
    name = forms.CharField(label = 'Name', max_length =  35)
    description = forms.CharField(label = 'Description', max_length = 120, widget=forms.Textarea)
    quantity = forms.IntegerField(label = 'Quantity', validators=[MinValueValidator(0),MaxValueValidator(50)])
