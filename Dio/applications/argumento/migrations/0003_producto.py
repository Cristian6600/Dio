# Generated by Django 3.2.5 on 2022-02-15 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('argumento', '0002_emision'),
    ]

    operations = [
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
