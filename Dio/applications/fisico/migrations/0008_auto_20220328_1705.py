# Generated by Django 3.2.5 on 2022-03-28 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0007_auto_20220328_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='destino',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='fisico',
            name='origen',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='destino',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='origen',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
