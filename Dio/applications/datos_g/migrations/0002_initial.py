# Generated by Django 3.2.5 on 2021-11-25 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos_g', '0001_initial'),
        ('guia', '0001_initial'),
        ('cliente', '0001_initial'),
        ('base_cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_g',
            name='cod_vis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.cod_vis'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='id_ciu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Id ciudad'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='id_estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='id_pro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_cliente.producto'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='mot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='datos_g.motivo', verbose_name='motivo'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='proceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.proceso'),
        ),
        migrations.AddField(
            model_name='datos_g',
            name='seudo_dg',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='guia.guia'),
        ),
    ]