# Generated by Django 3.2.5 on 2022-07-18 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0041_rastreo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rastreo',
            name='id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guia.guia'),
        ),
    ]
