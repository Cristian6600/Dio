# Generated by Django 3.2.5 on 2022-07-14 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0034_alter_telefono_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telefono',
            name='estado',
        ),
        migrations.AddField(
            model_name='telefono',
            name='estado_tel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
