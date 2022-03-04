# Generated by Django 3.2.5 on 2022-03-04 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argumento', '0002_nom_producto_nom_producto'),
        ('guia', '0003_historicalguia_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalguia',
            name='id_est',
            field=models.ForeignKey(blank=True, db_constraint=False, default=2, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.estado', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='historicalguia',
            name='mot',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.motivo', verbose_name='motivo'),
        ),
    ]
