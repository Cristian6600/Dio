# Generated by Django 3.2.5 on 2021-12-24 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0006_auto_20211224_1227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planilla',
            name='full_name',
        ),
    ]
