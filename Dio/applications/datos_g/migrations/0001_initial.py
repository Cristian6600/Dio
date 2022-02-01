# Generated by Django 3.2.5 on 2022-02-01 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cubrimiento',
            fields=[
                ('id_cubrimiento', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo')),
                ('oficina', models.CharField(max_length=80)),
                ('direccion', models.CharField(max_length=100)),
                ('dias', models.CharField(max_length=6)),
                ('direccion_cita', models.CharField(max_length=180)),
                ('postal', models.IntegerField()),
            ],
        ),
    ]
