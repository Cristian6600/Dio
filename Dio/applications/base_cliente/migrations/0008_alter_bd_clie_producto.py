# Generated by Django 3.2.5 on 2022-04-01 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argumento', '0001_initial'),
        ('base_cliente', '0007_bd_clie_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_clie',
            name='producto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.producto'),
        ),
    ]
