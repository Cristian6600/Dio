# Generated by Django 3.2.5 on 2021-07-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='est_clie',
            name='est_clie',
        ),
        migrations.AddField(
            model_name='est_clie',
            name='Descripcion',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='est_clie',
            name='Estado',
            field=models.CharField(default=1, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='est_clie',
            name='Proceso',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
