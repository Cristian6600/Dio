# Generated by Django 3.2.5 on 2022-06-16 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0001_initial'),
        ('ruta', '0022_auto_20220502_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planilla',
            name='full_name',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier', verbose_name='Mensajero'),
            preserve_default=False,
        ),
    ]
