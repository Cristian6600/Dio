# Generated by Django 3.2.5 on 2022-05-03 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_auto_20220503_1205'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'ordering': ['-ciudad']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='ciudad',
            order_with_respect_to=None,
        ),
    ]
