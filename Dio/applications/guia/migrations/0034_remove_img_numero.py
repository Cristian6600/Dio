# Generated by Django 3.2.5 on 2022-06-09 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0033_img_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='numero',
        ),
    ]
