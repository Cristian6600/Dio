# Generated by Django 3.2.5 on 2022-02-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0005_alter_historicalguia_id_guia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalguia',
            name='id_guia',
            field=models.IntegerField(blank=True, db_index=True),
        ),
    ]
