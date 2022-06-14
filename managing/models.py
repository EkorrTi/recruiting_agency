from tkinter import CASCADE
from django.db import models
from accounts.models import Account

# Create your models here.
class VacancyEmployer(models.Model):
    profession      = models.CharField(max_length=100)
    field           = models.CharField(max_length=100)
    experience      = models.DecimalField(max_digits=3, decimal_places=1)
    city            = models.CharField(max_length=100)
    remote_work     = models.BooleanField(default=False)
    salary          = models.DecimalField(max_digits=11, decimal_places=2)
    moving          = models.BooleanField(default=True)
    driver_license  = models.BooleanField(default=True)
    company         = models.CharField(max_length=200)
    employer        = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profession + '  -  ' + str(self.salary)

class VacancyEmployee(models.Model):
    profession      = models.CharField(max_length=100)
    field           = models.CharField(max_length=100)
    experience      = models.DecimalField(max_digits=3, decimal_places=1)
    city            = models.CharField(max_length=100)
    remote_work     = models.BooleanField(default=False)
    salary          = models.DecimalField(max_digits=11, decimal_places=2)
    moving          = models.BooleanField(default=True)
    driver_license  = models.BooleanField(default=True)
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.profession + '  -  ' + str(self.salary)