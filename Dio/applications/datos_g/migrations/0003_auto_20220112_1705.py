# Generated by Django 3.2.5 on 2022-01-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_g',
            name='autor',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Autorizado'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='d_i_a',
            field=models.IntegerField(blank=True, null=True, verbose_name='CC autorizado'),
        ),
    ]
