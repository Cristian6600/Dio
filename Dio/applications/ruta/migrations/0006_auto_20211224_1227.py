# Generated by Django 3.2.5 on 2021-12-24 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0005_cargue_pruebass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargue',
            name='pruebass',
        ),
        migrations.RemoveField(
            model_name='planilla',
            name='prueba',
        ),
    ]
