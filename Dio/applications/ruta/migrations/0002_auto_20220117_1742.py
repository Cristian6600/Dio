# Generated by Django 3.2.5 on 2022-01-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planilla',
            name='estado',
        ),
        migrations.AddField(
            model_name='planilla',
            name='estados',
            field=models.BooleanField(blank=True, default=1),
            preserve_default=False,
        ),
    ]