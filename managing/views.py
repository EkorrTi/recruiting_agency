from django_tables2 import SingleTableView
from django.shortcuts import render
from accounts.models import Account
from .models import *
from .tables import *
# Create your views here.
class EmployerVacancyListView(SingleTableView):
    model = VacancyEmployer
    table_class = EmployerVacancyTable
    template_name = 'managing.html'

# def manager_screen(request):
#     context = {}
#     accounts = Account.objects.all()
#     context['accounts'] = accounts

#     return render(request, 'base.html', context)