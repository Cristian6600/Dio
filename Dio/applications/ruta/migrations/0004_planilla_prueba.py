# Generated by Django 3.2.5 on 2021-12-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0003_planilla_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='planilla',
            name='prueba',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
