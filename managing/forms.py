from mimetypes import init
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *

class MakeVacancyEmployee(forms.ModelForm):
    profession  = forms.CharField(max_length=100)
    field       = forms.CharField(max_length=100)
    experience  = forms.DecimalField(max_digits=3, decimal_places=1)
    city        = forms.CharField(max_length=100)
    remote_work = forms.BooleanField(initial=False, required=False)
    salary      = forms.DecimalField(max_digits=11, decimal_places=2)
    moving      = forms.BooleanField(initial=False, required=False, label='Are you ready to move to a different town?')
    driver_license = forms.BooleanField(initial=False, required=False, label='Do you have a driver\'s license')
    class Meta:
        model = VacancyEmployee
        fields = ('profession', 'field', 'experience', 'city', 'remote_work', 'salary', 'moving', 'driver_license',)
        exclude = ('user',)

class MakeVacancyEmployer(forms.ModelForm):
    profession  = forms.CharField(max_length=100)
    field       = forms.CharField(max_length=100)
    experience  = forms.DecimalField(max_digits=3, decimal_places=1)
    city        = forms.CharField(max_length=100)
    remote_work = forms.BooleanField(initial=False, required=False)
    salary      = forms.DecimalField(max_digits=11, decimal_places=2)
    moving      = forms.BooleanField(initial=False, required=False, label='Is there a need to move to a different town?')
    driver_license = forms.BooleanField(initial=False, required=False, label='Is a driver\'s license needed?')
    company     = forms.CharField(max_length=100)
    class Meta:
        model = VacancyEmployee
        fields = ('profession', 'field', 'experience', 'city', 'remote_work', 'salary', 'moving', 'driver_license','company',)
        exclude = ('employer',)