# Generated by Django 3.2.5 on 2022-03-28 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guia', '0005_historicalguia_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalguia',
            name='fecha_descargue',
            field=models.DateField(blank=True, editable=False, null=True, verbose_name='Descargue'),
        ),
        migrations.AlterField(
            model_name='historicalguia',
            name='users',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario Descargue'),
        ),
    ]
