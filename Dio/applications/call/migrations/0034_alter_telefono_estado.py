# Generated by Django 3.2.5 on 2022-07-14 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0033_alter_telefono_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefono',
            name='estado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
