# Generated by Django 3.2.5 on 2022-01-18 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0004_fisico_est_planilla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisico',
            name='est_planilla',
            field=models.CharField(max_length=30),
        ),
    ]
