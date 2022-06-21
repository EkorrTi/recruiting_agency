from dataclasses import field, fields
import django_filters
from .models import *

class EmprVacFilter(django_filters.FilterSet):
    class Meta:
        model = VacancyEmployer
        fields = ('profession', 'field', 'salary', 'city', 'remote_work', 'moving', 'driver_license')

class EmpeVacFilter(django_filters.FilterSet):
    class Meta:
        model = VacancyEmployee
        fields = ('profession', 'field', 'salary', 'city', 'remote_work', 'moving', 'driver_license')