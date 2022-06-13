# Generated by Django 3.2.8 on 2022-06-13 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='VacancyEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
                ('experience', models.DecimalField(decimal_places=1, max_digits=3)),
                ('city', models.CharField(max_length=100)),
                ('remote_work', models.BooleanField(default=False)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=11)),
                ('moving', models.BooleanField(default=True)),
                ('driver_license', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyEmployer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('field', models.CharField(max_length=100)),
                ('experience', models.DecimalField(decimal_places=1, max_digits=3)),
                ('city', models.CharField(max_length=100)),
                ('remote_work', models.BooleanField(default=False)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=11)),
                ('moving', models.BooleanField(default=True)),
                ('driver_license', models.BooleanField(default=True)),
                ('company', models.CharField(max_length=200)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]