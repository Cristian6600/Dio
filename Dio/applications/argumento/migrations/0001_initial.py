# Generated by Django 3.2.5 on 2022-02-16 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cod_vis',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo de visita')),
                ('visita', models.CharField(max_length=36)),
                ('tipo', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Emision',
            fields=[
                ('t_emi', models.CharField(max_length=4, primary_key=True, serialize=False, verbose_name='Tipo emision')),
                ('emision', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Emision',
                'verbose_name_plural': 'Emision',
            },
        ),
        migrations.CreateModel(
            name='Est_clie',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cod_est', models.IntegerField()),
                ('estado', models.CharField(max_length=55)),
                ('descripcion', models.CharField(max_length=55)),
                ('proceso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Estado', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Nom_producto',
            fields=[
                ('id', models.CharField(max_length=3, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('proceso', models.CharField(max_length=30)),
                ('cod_dir', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id_tip', models.IntegerField(primary_key=True, serialize=False)),
                ('Tipo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Tipo',
                'verbose_name_plural': 'Tipo',
            },
        ),
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=50)),
                ('id_tip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.tipo')),
            ],
            options={
                'verbose_name': 'Motivo',
                'verbose_name_plural': 'Motivo',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_pro', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Id producto')),
                ('producto', models.CharField(max_length=50)),
                ('proceso', models.CharField(blank=True, max_length=50, null=True)),
                ('tipo', models.CharField(blank=True, max_length=5, null=True, verbose_name='Tipos distribucion')),
                ('homologacion', models.CharField(blank=True, max_length=50, null=True)),
                ('id_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Id cliente')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Producto',
                'unique_together': {('id_pro', 'id_clie')},
            },
        ),
    ]
