# Generated by Django 3.2.5 on 2022-04-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicativo',
            name='ind',
            field=models.CharField(max_length=10, verbose_name='Indicativo'),
        ),
    ]