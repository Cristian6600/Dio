# Generated by Django 3.2.5 on 2022-01-17 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0002_initial'),
        ('ruta', '0003_alter_planilla_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla',
            name='guia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
            preserve_default=False,
        ),
    ]
