# Generated by Django 3.2.5 on 2022-06-24 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0012_auto_20220624_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_clie',
            name='fisicos',
            field=models.CharField(choices=[('1', 'Fisico'), ('2', 'No llego fisico'), ('3', 'Fisico paquete')], max_length=8),
        ),
    ]
