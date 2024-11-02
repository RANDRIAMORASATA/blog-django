from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomUserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control my-2'
        self.fields['password'].widget.attrs['class'] = 'form-control my-2'

    