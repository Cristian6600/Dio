# Generated by Django 3.2.5 on 2022-01-17 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0002_auto_20220117_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla',
            name='estados',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]
