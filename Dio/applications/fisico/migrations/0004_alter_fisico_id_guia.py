# Generated by Django 3.2.5 on 2022-02-02 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0003_alter_fisico_id_guia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisico',
            name='id_guia',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
