from django_tables2 import RequestConfig, SingleTableView
from django.shortcuts import render, redirect
from accounts.models import Account
from managing.forms import MakeVacancyEmployee, MakeVacancyEmployer
from .models import *
from .tables import *
# Create your views here.
def manager_screen(request):
    
    eeTable = EmployeeVacancyTable( data=VacancyEmployee.objects.all(), prefix='Empe-' )
    erTable = EmployerVacancyTable( data=VacancyEmployer.objects.all(), prefix='Empr-' )

    RequestConfig(request, paginate=False).configure(eeTable)
    RequestConfig(request, paginate=False).configure(erTable)

    context = {
        'eeTable': eeTable,
        'erTable': erTable
    }

    return render(request, 'managing.html', context)

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import *
class FilteredEmployerTable(SingleTableMixin, FilterView):
    table_class = EmployerVacancyTable
    model = VacancyEmployer
    template_name = 'register.html'
    filtered_class = EmprVacFilter

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
