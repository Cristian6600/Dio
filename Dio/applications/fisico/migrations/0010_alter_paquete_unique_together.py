# Generated by Django 3.2.5 on 2022-01-28 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0001_initial'),
        ('fisico', '0009_alter_paquete_seudo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='paquete',
            unique_together={('bolsa', 'seudo')},
        ),
    ]