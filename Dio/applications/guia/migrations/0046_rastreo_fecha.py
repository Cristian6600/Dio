# Generated by Django 3.2.5 on 2022-07-18 21:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0045_alter_rastreo_motivopr'),
    ]

    operations = [
        migrations.AddField(
            model_name='rastreo',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
