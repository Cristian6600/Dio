# Generated by Django 3.2.5 on 2021-08-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0003_alter_bd_clie_guia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_clie',
            name='Seudo',
            field=models.CharField(max_length=35, primary_key=True, serialize=False, unique=True),
        ),
    ]
