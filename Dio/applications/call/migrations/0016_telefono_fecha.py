# Generated by Django 3.2.5 on 2022-05-20 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0015_auto_20220517_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
