# Generated by Django 3.2.5 on 2022-04-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0003_datos_g_cantidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='nombre_orden',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
