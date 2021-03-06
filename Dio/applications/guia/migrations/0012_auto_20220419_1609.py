# Generated by Django 3.2.5 on 2022-04-19 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20220317_1511'),
        ('guia', '0011_auto_20220419_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='oficina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.oficinas'),
        ),
        migrations.AddField(
            model_name='historicalguia',
            name='oficina',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cliente.oficinas'),
        ),
    ]
