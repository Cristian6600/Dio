# Generated by Django 3.2.5 on 2022-03-17 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisico',
            name='fecha_planilla',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalfisico',
            name='fecha_planilla',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
