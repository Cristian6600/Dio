# Generated by Django 3.2.5 on 2022-07-18 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0043_auto_20220718_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rastreo',
            name='id_guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.guia'),
        ),
    ]