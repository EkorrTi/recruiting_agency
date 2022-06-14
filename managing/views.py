from django_tables2 import RequestConfig, SingleTableView
from django.shortcuts import render
from accounts.models import Account
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