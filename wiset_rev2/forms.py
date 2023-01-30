from django import forms
from django.core.validators import MinValueValidator


class MoneyForm(forms.Form):
    money_amount = forms.DecimalField(
        max_digits=6,
        decimal_places=2,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[MinValueValidator(0)],
    )


class ProductForm(forms.Form):
    id = forms.IntegerField(min_value=1, widget=forms.HiddenInput())
    name = forms.CharField(max_length=50)
    price = forms.DecimalField(
        max_digits=6, decimal_places=2, validators=[MinValueValidator(0)]
    )
    category = forms.CharField(max_length=50)
    in_fridge = forms.BooleanField(required=False)
