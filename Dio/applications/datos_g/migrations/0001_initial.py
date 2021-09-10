# Generated by Django 3.2.5 on 2021-09-06 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_cliente', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='datos_g',
            fields=[
                ('id', models.OneToOneField(help_text='Codigo de barras', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base_cliente.bd_clie', verbose_name='seudo')),
                ('bolsa', models.IntegerField(help_text='Codigo de barras')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha fisico')),
                ('d_i', models.BigIntegerField(blank=True, null=True, verbose_name='Documento de identidad')),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('postal', models.CharField(blank=True, max_length=7, null=True)),
                ('barrio', models.CharField(blank=True, max_length=70, null=True)),
                ('marca', models.CharField(blank=True, max_length=15, null=True)),
                ('gx', models.BigIntegerField(blank=True, null=True)),
                ('gy', models.BigIntegerField(blank=True, null=True)),
                ('id_ciu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Id ciudad')),
                ('id_pro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_cliente.producto')),
            ],
            options={
                'verbose_name': 'Datos de gestion',
                'verbose_name_plural': 'Datos de gestion',
            },
        ),
    ]
