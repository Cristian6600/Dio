# Generated by Django 3.2.5 on 2022-03-28 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ruta', '0016_destino_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destino',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.sucursales'),
        ),
    ]
