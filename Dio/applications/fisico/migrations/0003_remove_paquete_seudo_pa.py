# Generated by Django 3.2.5 on 2021-08-12 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0002_alter_paquete_seudo_pa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete',
            name='seudo_pa',
        ),
    ]
