from django.forms import *
from django import forms
from App.models import SubStores, Stores
from App.functions import get_sub_stores


class RegisterForm(Form):
    CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    YEARS = [x for x in range(1940, 2021)]

    first_name = forms.CharField(max_length=60, required=True, widget=TextInput)
    last_name = forms.CharField(max_length=60, required=True, widget=TextInput)
    gender = forms.ChoiceField(choices=CHOICES)
    date_of_birth = forms.DateTimeField(widget=forms.SelectDateWidget(years=YEARS), required=True)
    email = forms.EmailField(widget=EmailInput)
    password = forms.CharField(required=True, widget=PasswordInput)


class LoginForm(Form):
    email = forms.EmailField(widget=EmailInput)
    password = forms.CharField(required=True, widget=PasswordInput)



class CalculateFormRL(Form):
    code = ''
    sub_store_list = get_sub_stores('רמי לוי')
    sub_store = forms.ChoiceField(choices=sub_store_list)


class CalculateFormVIC(Form):
    code = ''
    sub_store_list = get_sub_stores('ויקטורי')
    sub_store = forms.ChoiceField(choices=sub_store_list)


class CalculateFormY(Form):
    code = ''
    sub_store_list = get_sub_stores('יוחננוף')
    sub_store = forms.ChoiceField(choices=sub_store_list)

