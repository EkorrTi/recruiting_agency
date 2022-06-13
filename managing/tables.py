from dataclasses import fields
import django_tables2 as tables
from .models import *

class EmployerVacancyTable(tables.Table):
    class Meta:
        model = VacancyEmployer
        template_name = 'managing.html'
        fields = ('profession', 'field', 'salary')