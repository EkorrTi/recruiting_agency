import django_filters
from .models import *

class EmprVacFilter(django_filters.FilterSet):
    class Meta:
        model = VacancyEmployer
        fields = ['profession', 'field', 'salary', 'remote_work']