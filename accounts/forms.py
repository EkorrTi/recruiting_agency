from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Account

class RegistrationForm(UserCreationForm):
    email       = forms.EmailField(help_text='Required')
    
    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2', 'is_manager', 'is_employer')