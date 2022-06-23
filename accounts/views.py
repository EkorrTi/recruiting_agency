from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
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

def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        if user.is_admin: return redirect('/admin')
        if user.is_manager: return redirect('manager')
        if user.is_employer: return redirect('employerPost')
        return redirect('employeePost')
    
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request=request, user=user)
                if user.is_admin: return redirect('/admin')
                if user.is_manager: return redirect('manager')
                if user.is_employer: return redirect('employerPost')
                return redirect('employeePost')
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')