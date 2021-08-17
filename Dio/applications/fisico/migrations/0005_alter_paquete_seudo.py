# Generated by Django 3.2.5 on 2021-08-17 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0004_alter_bd_clie_seudo'),
        ('fisico', '0004_alter_paquete_seudo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='Seudo',
            field=models.ForeignKey(help_text='Codigo de barras', on_delete=django.db.models.deletion.CASCADE, to='base_cliente.bd_clie', unique=True),
        ),
    ]
