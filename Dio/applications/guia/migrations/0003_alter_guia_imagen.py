# Generated by Django 3.2.5 on 2021-08-14 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0002_alter_guia_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guia',
            name='Imagen',
            field=models.ImageField(blank=True, null=True, upload_to='guia'),
        ),
    ]
