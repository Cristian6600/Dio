# Generated by Django 3.2.5 on 2022-05-23 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0025_alter_telefono_indicativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='fecha_call',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
