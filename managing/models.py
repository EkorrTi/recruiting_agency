from tkinter import CASCADE
from django.db import models
from pkg_resources import resource_filename
from accounts.models import Account
profession_choices = (
    ('Android-dev', 'Android developer'),
    ('Driver', 'Driver'),
    ('Back-end dev', 'Back-End developer'),
    ('Accountant', 'Accountant'),
    ('Lawyer', 'Lawyer'),
    ('Cashier', 'Cashier'),
)

city_choices = (
    ('Almaty', 'Almaty, Kazakhstan'),
    ('Astana', 'Astana, Kazakhstan'),
    ('Karagandy', 'Karagandy, Kazakhstan'),
    ('Moscow', 'Moscow, Russia'),
)

workmodel_choices = (
    ('Full time employment', 'Full employment'),
    ('Single project', 'Single project (freelance)'),
    ('Internship', 'Internship'),
)

def user_directory_path(instance, filename):

	# file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
	return 'user_{0}/{1}'.format(instance.user.email, filename)

# Create your models here.
class VacancyEmployer(models.Model):
    profession      = models.CharField(max_length=100, choices=profession_choices)
    experience      = models.DecimalField(max_digits=3, decimal_places=1)
    city            = models.CharField(max_length=100, choices=city_choices)
    remote_work     = models.BooleanField(default=False)
    work_model      = models.CharField(max_length=100, choices=workmodel_choices, default='Full time employment')
    salary          = models.DecimalField(max_digits=11, decimal_places=2)
    moving          = models.BooleanField(default=True)
    driver_license  = models.BooleanField(default=True)
    smoking         = models.BooleanField(default=True)
    company         = models.CharField(max_length=200)
    employer        = models.ForeignKey(Account, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profession + '  -  ' + str(self.salary)

class VacancyEmployee(models.Model):
    profession      = models.CharField(max_length=100, choices=profession_choices)
    experience      = models.DecimalField(max_digits=3, decimal_places=1)
    city            = models.CharField(max_length=100, choices=city_choices)
    remote_work     = models.BooleanField(default=False)
    work_model      = models.CharField(max_length=100, choices=workmodel_choices, default='Full time employment')
    salary          = models.DecimalField(max_digits=11, decimal_places=2)
    moving          = models.BooleanField(default=True)
    driver_license  = models.BooleanField(default=True)
    smoking         = models.BooleanField(default=True)
    resume          = models.FileField(blank=True, null=True, upload_to=user_directory_path)
    user            = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.profession + '  -  ' + str(self.salary)