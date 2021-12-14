# Generated by Django 3.2.5 on 2021-12-09 22:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
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
            name='Producto',
            fields=[
                ('id_pro', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Id producto')),
                ('producto', models.CharField(max_length=50)),
                ('Proceso', models.CharField(blank=True, max_length=50, null=True)),
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
        migrations.CreateModel(
            name='Bd_clie',
            fields=[
                ('seudo_bd', models.CharField(max_length=35, primary_key=True, serialize=False)),
                ('archivo', models.CharField(blank=True, max_length=15, null=True)),
                ('jornada', models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], max_length=3, null=True)),
                ('d_i', models.CharField(blank=True, max_length=13, null=True, verbose_name='Documento de identidad')),
                ('cliente', models.CharField(blank=True, max_length=150, null=True)),
                ('id_proc', models.IntegerField(blank=True, null=True)),
                ('ofi', models.CharField(blank=True, max_length=8, null=True, verbose_name='Oficina')),
                ('canal', models.CharField(blank=True, max_length=8, null=True)),
                ('realz', models.CharField(blank=True, max_length=30, null=True, verbose_name='Realzador')),
                ('tipo', models.CharField(blank=True, max_length=30, null=True)),
                ('d_i_a', models.IntegerField(blank=True, null=True, verbose_name='CC autorizado')),
                ('autor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autorizado')),
                ('tarjeta', models.CharField(blank=True, max_length=30, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('referencia', models.CharField(blank=True, max_length=50, null=True)),
                ('convenio', models.CharField(blank=True, max_length=50, null=True)),
                ('id_serv', models.IntegerField(verbose_name='Id Servicio')),
                ('bolsa', models.IntegerField(blank=True, null=True)),
                ('guia', models.IntegerField(blank=True, null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('fe_fisico', models.DateTimeField(blank=True, null=True, verbose_name='Fecha fisico')),
                ('sucursal', models.CharField(blank=True, max_length=50, null=True)),
                ('id_clie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente', verbose_name='Id cliente')),
                ('id_est_clie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_cliente.est_clie', verbose_name='Id estado cliente ')),
                ('id_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_cliente.producto', verbose_name='Id producto')),
                ('t_emi', models.ForeignKey(max_length=4, on_delete=django.db.models.deletion.CASCADE, to='base_cliente.emision', verbose_name='Tipo Emision')),
            ],
            options={
                'verbose_name': 'Base Cliente',
                'verbose_name_plural': 'Base Cliente',
            },
        ),
    ]
