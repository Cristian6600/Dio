# Generated by Django 3.2.5 on 2022-03-17 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oficinas',
            name='hora_adi',
            field=models.CharField(max_length=90, verbose_name='Horario adicional'),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='hora_norm',
            field=models.CharField(max_length=90, verbose_name='Horario normal'),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='hora_sab',
            field=models.CharField(max_length=90, verbose_name='Horario sabado'),
        ),
        migrations.AlterField(
            model_name='oficinas',
            name='nom_ofi',
            field=models.CharField(max_length=80),
        ),
    ]
