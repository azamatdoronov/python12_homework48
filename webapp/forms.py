from django import forms
from django.forms import widgets

CATEGORY_CHOICES = [('other', 'разное'), ('bakery', 'выпечка'), ('sweets', 'сладости'),
                    ('drinks', 'напитки'), ('veggies', 'овощи')]


class ProductForm(forms.Form):
    category = forms.ChoiceField(required=True, choices=CATEGORY_CHOICES, label="Категория:")
    p_name = forms.CharField(max_length=100, required=True, label='Имя товара:')
    description = forms.CharField(max_length=2000, required=False, label='Описание:',
                                  widget=widgets.Textarea(attrs={"cols": 45, "rows": 3}))
    balance = forms.IntegerField(min_value=1, label="Остаток:")
    price = forms.DecimalField(max_digits=9, decimal_places=2, label="Цена:")
