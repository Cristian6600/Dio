# Generated by Django 3.2.5 on 2022-02-15 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0010_remove_bd_clie_id_pro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bd_clie',
            name='fecha_recepcion',
        ),
    ]