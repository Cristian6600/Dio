# Generated by Django 3.2.5 on 2022-05-20 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0008_auto_20220520_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos_g',
            name='fecha_call',
        ),
        migrations.RemoveField(
            model_name='datos_g',
            name='motivo_call',
        ),
        migrations.RemoveField(
            model_name='datos_g',
            name='observacion',
        ),
    ]