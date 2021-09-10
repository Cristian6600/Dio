# Generated by Django 3.2.5 on 2021-09-09 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base_cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bd_clie',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user'),
            preserve_default=False,
        ),
    ]
