# Generated by Django 3.2.5 on 2022-04-02 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0008_auto_20220328_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalguia',
            name='fecha_bolsa',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
