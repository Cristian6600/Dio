# Generated by Django 3.2.5 on 2022-07-14 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0035_auto_20220714_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefono',
            old_name='estado_tel',
            new_name='estado',
        ),
    ]
