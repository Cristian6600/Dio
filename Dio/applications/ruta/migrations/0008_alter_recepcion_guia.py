# Generated by Django 3.2.5 on 2022-01-18 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0002_initial'),
        ('ruta', '0007_auto_20220118_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recepcion',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
        ),
    ]
