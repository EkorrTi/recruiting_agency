from django_tables2 import RequestConfig, SingleTableView
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django_tables2.views import MultiTableMixin
from accounts.models import Account
from .forms import MakeVacancyEmployee, MakeVacancyEmployer
from .models import *
from .tables import *
from .filters import *
# Create your views here.
def manager_screen(request):
    
    eeFilter = EmpeVacFilter(request.GET, queryset=VacancyEmployee.objects.all())
    erFilter = EmprVacFilter(request.GET, queryset=VacancyEmployer.objects.all())
    eeTable = EmployeeVacancyTable( data=eeFilter.qs, prefix='Empe-' )
    erTable = EmployerVacancyTable( data=erFilter.qs, prefix='Empr-' )

    RequestConfig(request, paginate=False).configure(eeTable)
    RequestConfig(request, paginate=False).configure(erTable)

    context = {
        'eeTable': eeTable,
        'erTable': erTable,
        'filter' : erFilter
    }

    return render(request, 'managing.html', context)

def postVacancyEmployee(request):
    context = {}
    user = request.user

    if not user.is_authenticated:
        return redirect('manager')
    
    if request.POST:
        form = MakeVacancyEmployee(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.user = user
            vacancy.save()
            return redirect('manager')
        else:
            context['form'] = form
    else:
        form = MakeVacancyEmployee()
        context['form'] = form
    return render(request, 'employee.html', context)

def postVacancyEmployer(request):
    context = {}
    user = request.user

    if not user.is_employer: redirect('register')

    if request.POST:
        form = MakeVacancyEmployer(request.POST)
        if form.is_valid():
            vacancy = form.save(commit=False)
            vacancy.employer = user
            vacancy.save()
            return redirect('manager')
        else:
            context['form'] = form
    else:
        context['form'] = MakeVacancyEmployer()
    return render(request, 'employer.html', context)
