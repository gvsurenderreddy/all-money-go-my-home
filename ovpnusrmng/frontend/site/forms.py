from django import forms
from django.forms import ModelForm

from backend.usercontrol.models import User

class LoginForm(ModelForm):
    class Meta:
	model = User
	fields = ('Username', 'Password')
   
    Password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(ModelForm):
    class Meta:
	model = User

    Password = forms.CharField(widget=forms.PasswordInput)
