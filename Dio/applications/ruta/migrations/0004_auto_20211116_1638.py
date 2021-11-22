# Generated by Django 3.2.5 on 2021-11-16 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0001_initial'),
        ('ruta', '0003_auto_20211116_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargue',
            name='mensajero',
        ),
        migrations.RemoveField(
            model_name='planilla',
            name='guia',
        ),
        migrations.AddField(
            model_name='planilla',
            name='mensajero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier'),
            preserve_default=False,
        ),
    ]