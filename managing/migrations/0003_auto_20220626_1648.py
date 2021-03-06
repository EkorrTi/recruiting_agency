# Generated by Django 3.2.8 on 2022-06-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managing', '0002_vacancyemployee_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancyemployee',
            name='field',
        ),
        migrations.RemoveField(
            model_name='vacancyemployer',
            name='field',
        ),
        migrations.AlterField(
            model_name='vacancyemployee',
            name='city',
            field=models.CharField(choices=[('Almaty', 'Almaty'), ('Astana', 'Astana'), ('Karagandy', 'Karagandy'), ('Moscow', 'Moscow')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancyemployee',
            name='profession',
            field=models.CharField(choices=[('Android-dev', 'Android developer'), ('Driver', 'Driver'), ('Back-end dev', 'Back-End developer'), ('Accountant', 'Acountant'), ('Lawyer', 'Lawyer'), ('Cashier', 'Cashier')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancyemployer',
            name='city',
            field=models.CharField(choices=[('Almaty', 'Almaty'), ('Astana', 'Astana'), ('Karagandy', 'Karagandy'), ('Moscow', 'Moscow')], max_length=100),
        ),
        migrations.AlterField(
            model_name='vacancyemployer',
            name='profession',
            field=models.CharField(choices=[('Android-dev', 'Android developer'), ('Driver', 'Driver'), ('Back-end dev', 'Back-End developer'), ('Accountant', 'Acountant'), ('Lawyer', 'Lawyer'), ('Cashier', 'Cashier')], max_length=100),
        ),
    ]
