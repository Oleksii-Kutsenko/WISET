from django import forms
from django.core.validators import MinValueValidator


class MoneyForm(forms.Form):
    money_amount = forms.DecimalField(max_digits=6, decimal_places=2,
                                      widget=forms.TextInput(attrs={'class': 'form-control'}),
                                      validators=[MinValueValidator(0)])
