# Generated by Django 3.2.5 on 2022-02-15 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0006_alter_datos_g_dest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datos_g',
            name='lote',
        ),
    ]