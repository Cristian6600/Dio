# Generated by Django 3.2.5 on 2022-05-21 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0024_alter_telefono_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='indicativo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='call.indicativo'),
        ),
    ]
