# Generated by Django 3.2.5 on 2022-03-25 19:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guia', '0004_alter_historicalguia_fecha_planilla'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalguia',
            name='users',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
