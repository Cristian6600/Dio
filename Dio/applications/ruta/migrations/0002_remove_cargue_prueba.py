# Generated by Django 3.2.5 on 2021-11-30 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargue',
            name='prueba',
        ),
    ]
