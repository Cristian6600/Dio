# Generated by Django 3.2.5 on 2022-01-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0005_alter_fisico_est_planilla'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='id_planilla',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]