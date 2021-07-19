# Generated by Django 3.2.5 on 2021-07-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mot', models.IntegerField()),
                ('motivo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Datos de gestion',
                'verbose_name_plural': 'Datos de gestion',
            },
        ),
        migrations.CreateModel(
            name='datos_g',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Seudo', models.CharField(max_length=35)),
                ('direccion', models.CharField(max_length=255)),
                ('postal', models.CharField(max_length=7)),
                ('barrio', models.CharField(blank=True, max_length=70, null=True)),
                ('gx', models.BigIntegerField(blank=True, null=True)),
                ('gy', models.BigIntegerField(blank=True, null=True)),
                ('id_ciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad')),
                ('id_mot', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datos_g.motivo')),
            ],
            options={
                'verbose_name': 'Datos de gestion',
                'verbose_name_plural': 'Datos de gestion',
            },
        ),
    ]
