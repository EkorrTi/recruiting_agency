from dataclasses import fields
import django_tables2 as tables
from django_filters.views import FilterView
from .models import *

class EmployerVacancyTable(tables.Table):
    class Meta:
        model = VacancyEmployer

class EmployeeVacancyTable(tables.Table):
    class Meta:
        model = VacancyEmployee