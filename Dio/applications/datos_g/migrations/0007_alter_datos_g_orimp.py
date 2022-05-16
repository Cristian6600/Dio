# Generated by Django 3.2.5 on 2022-05-12 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0006_alter_datos_g_orimp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_g',
            name='orimp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orden_datos_g', related_query_name='orden_dat_g', to='datos_g.orden', verbose_name='Orden impresion'),
        ),
    ]
