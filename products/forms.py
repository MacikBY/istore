from django import forms
from django.core.exceptions import ValidationError

from products.models import Contact


def phone_number_validator(phone_number):
    # print(type(phone_number[4:6]), '25')
    if phone_number.startswith('+375') and (phone_number[4:6] in ['25', '29', '33', '44']):
        return phone_number
    else:
        raise ValidationError('Неправильный номер телефона')


class ContactModelForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=13, validators=[phone_number_validator])

    class Meta:
        model = Contact
        fields = ('name', 'phone_number',)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=13, validators=[phone_number_validator])
