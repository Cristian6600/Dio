# Generated by Django 3.2.5 on 2021-07-25 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='vehiculo',
            fields=[
                ('id_veg', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id vehiculo')),
                ('vehiculo', models.CharField(max_length=35)),
                ('Marca', models.CharField(max_length=20)),
                ('cilindraje', models.IntegerField()),
                ('capacidad', models.IntegerField()),
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
                ('id_courrier', models.IntegerField(verbose_name='Id Courrier')),
                ('d_i', models.BigIntegerField()),
                ('Courrier', models.CharField(max_length=70, verbose_name='Nombre courrier')),
                ('Cel', models.IntegerField(verbose_name='Celular')),
                ('dir', models.CharField(max_length=120)),
                ('id_veh', models.IntegerField(verbose_name='Id vehiculo')),
                ('placa', models.IntegerField()),
                ('soat', models.CharField(max_length=25)),
                ('tecnomecanica', models.BooleanField(default=False)),
                ('infraccion', models.IntegerField()),
                ('modelo', models.DateField()),
                ('licencia', models.IntegerField()),
                ('id_ciu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Id ciudad')),
            ],
            options={
                'verbose_name': 'Courrier',
                'verbose_name_plural': 'Courrier',
            },
        ),
    ]