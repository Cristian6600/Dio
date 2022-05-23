# Generated by Django 3.2.5 on 2022-05-20 20:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('call', '0021_auto_20220520_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefono',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario call'),
        ),
    ]
