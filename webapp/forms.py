from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from webapp.models import Product, Cart, Order


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Найти')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ["qty"]


# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = ["name", "phone", "address"]
#

class OrderForm(ModelForm):
    def __init__(self, user=None, **kwargs):
        self.user = user
        if user and not user.is_authenticated:
            self.user = None
        super().__init__(**kwargs)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not self.user and not self.cleaned_data.get('name'):
            raise ValidationError('Необходимо указать логин либо его имя')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not self.user and not self.cleaned_data.get('email'):
            raise ValidationError('Необходимо авторизоваться или указать ваш email')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not self.user and not self.cleaned_data.get('phone'):
            raise ValidationError('Необходимо авторизоваться или указать Ваш номер телефона')
        return phone

    class Meta:
        model = Order
        fields = ['user', 'name', 'phone']
