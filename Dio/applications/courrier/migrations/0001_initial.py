# Generated by Django 3.2.5 on 2022-02-03 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id_veg', models.AutoField(primary_key=True, serialize=False, verbose_name='Id vehiculo')),
                ('name', models.CharField(max_length=50, verbose_name='Propietario de vehiculo')),
                ('cc', models.CharField(max_length=13)),
                ('vehiculo', models.CharField(max_length=35)),
                ('marca', models.CharField(max_length=20)),
                ('cilindraje', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('modelo', models.DateField()),
                ('placa', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculo',
            },
        ),
        migrations.CreateModel(
            name='courrier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_i', models.CharField(max_length=12)),
                ('courrier', models.CharField(max_length=70, verbose_name='Nombre courrier')),
                ('cel', models.CharField(max_length=12, verbose_name='Celular')),
                ('dir', models.CharField(max_length=120)),
                ('soat', models.CharField(max_length=25)),
                ('tecnomecanica', models.BooleanField(default=False)),
                ('infraccion', models.IntegerField()),
                ('licencia', models.IntegerField()),
                ('id_ciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Id ciudad')),
                ('id_veh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.vehiculo', verbose_name='Id vehiculo')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.marca_vehiculo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.tipo_vehiculo', verbose_name='Tipo vehiculo')),
            ],
            options={
                'verbose_name': 'Courrier',
                'verbose_name_plural': 'Courrier',
            },
        ),
    ]
