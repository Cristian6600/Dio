# Generated by Django 3.2.5 on 2021-09-07 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0001_initial'),
        ('ruta', '0004_alter_cargue_mensajero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargue',
            name='mensajero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier'),
        ),
    ]
