# Generated by Django 3.2.5 on 2022-05-03 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_alter_ciudad_departamento'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={},
        ),
        migrations.AlterOrderWithRespectTo(
            name='ciudad',
            order_with_respect_to='ciudad',
        ),
    ]