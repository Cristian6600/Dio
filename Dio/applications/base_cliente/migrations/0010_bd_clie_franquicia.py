# Generated by Django 3.2.5 on 2022-05-23 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argumento', '0008_franquicia'),
        ('base_cliente', '0009_alter_bd_clie_fisicos'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd_clie',
            name='franquicia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.franquicia'),
        ),
    ]