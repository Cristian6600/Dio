# Generated by Django 3.2.5 on 2022-02-15 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0011_remove_bd_clie_fecha_recepcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bd_clie',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='bd_clie',
            name='d_i',
        ),
    ]
