# Generated by Django 3.2.5 on 2022-05-20 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('call', '0017_alter_telefono_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='observacion',
            field=models.TextField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
