# Generated by Django 3.2.5 on 2022-04-02 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_g',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
