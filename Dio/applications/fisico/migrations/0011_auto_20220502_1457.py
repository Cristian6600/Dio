# Generated by Django 3.2.5 on 2022-05-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0010_auto_20220402_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='estado_destino',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='estado_destino',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]