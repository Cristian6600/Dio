# Generated by Django 3.2.5 on 2022-05-20 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0014_auto_20220516_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guia',
            name='observacion',
        ),
        migrations.RemoveField(
            model_name='historicalguia',
            name='observacion',
        ),
    ]