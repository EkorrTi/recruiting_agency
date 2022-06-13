from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from accounts.forms import *

# Create your views here.
def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_pass = form.cleaned_data.get('password1')
            is_manager = form.cleaned_data.get('is_manager')
            is_employer = form.cleaned_data.get('is_employer')
            account = authenticate(email=email, password=raw_pass)
            login(request, account)
            return redirect('manager')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'register.html', context)