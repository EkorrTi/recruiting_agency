import django_filters
from .models import *

class EmprVacFilter(django_filters.FilterSet):
    profession = django_filters.AllValuesFilter()
    experience = django_filters.NumberFilter(label='Experience range (years)', lookup_expr='gte')
    salary = django_filters.NumberFilter(label='Salary range', lookup_expr='gte')
    city = django_filters.AllValuesFilter()
    company = django_filters.AllValuesFilter()

    class Meta:
        model = VacancyEmployer
        fields = ('profession', 'experience', 'salary', 'city', 'remote_work', 'moving', 'driver_license', 'smoking')

class EmpeVacFilter(django_filters.FilterSet):
    profession = django_filters.AllValuesFilter()
    experience = django_filters.NumberFilter(lookup_expr='gte')
    salary = django_filters.NumberFilter(lookup_expr='gte')
    city = django_filters.AllValuesFilter()

    class Meta:
        model = VacancyEmployee
        fields = ('profession', 'experience',  'salary', 'city', 'remote_work', 'moving', 'driver_license', 'smoking')
        exclude = ('resume',)