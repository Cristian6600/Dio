# Generated by Django 3.2.5 on 2021-09-06 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='paquete',
            fields=[
                ('seudo', models.OneToOneField(help_text='Codigo de barras', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base_cliente.bd_clie')),
                ('bolsa', models.IntegerField(help_text='Codigo de barras')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
    ]
