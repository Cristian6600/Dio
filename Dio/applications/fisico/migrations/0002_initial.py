# Generated by Django 3.2.5 on 2021-12-03 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fisico', '0001_initial'),
        ('guia', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='cod_vis',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.cod_vis'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='id_ciu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='ciudad'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='id_est',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='proceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.proceso'),
        ),
    ]
