# Generated by Django 3.2.5 on 2022-02-15 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('argumento', '0003_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Est_clie',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cod_est', models.IntegerField()),
                ('estado', models.CharField(max_length=55)),
                ('descripcion', models.CharField(max_length=55)),
                ('proceso', models.CharField(max_length=20)),
            ],
        ),
    ]