from mimetypes import init
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from .models import *

class MakeVacancyEmployer(forms.ModelForm):
    experience  = forms.DecimalField(max_digits=3, decimal_places=1, label='Experience(years)')
    remote_work = forms.BooleanField(initial=False, required=False)
    salary      = forms.DecimalField(max_digits=11, decimal_places=2)
    moving      = forms.BooleanField(initial=False, required=False, label='Is there a need to move to a different town?')
    driver_license = forms.BooleanField(initial=False, required=False, label='Is a driver\'s license needed?')
    smoking     = forms.BooleanField(initial=False, required=False, label='Is smoking allowed?')
    company     = forms.CharField(max_length=100)
    class Meta:
        model = VacancyEmployer
        fields = ('profession', 'experience', 'city', 'remote_work', 'work_model', 'salary', 'moving', 'driver_license', 'company', 'smoking')
        exclude = ('employer',)

class MakeVacancyEmployee(forms.ModelForm):
    experience  = forms.DecimalField(max_digits=3, decimal_places=1, label='Experience(years)')
    remote_work = forms.BooleanField(initial=False, required=False)
    salary      = forms.DecimalField(max_digits=11, decimal_places=2)
    moving      = forms.BooleanField(initial=False, required=False, label='Are you ready to move to a different town?')
    driver_license = forms.BooleanField(initial=False, required=False, label='Do you have a driver\'s license')
    smoking     = forms.BooleanField(initial=False, required=False, label='Do you smoke?')
    class Meta:
        model = VacancyEmployee
        fields = ('profession', 'experience', 'city', 'remote_work', 'work_model', 'salary', 'moving', 'driver_license', 'smoking', 'resume')
        exclude = ('user',)