# Generated by Django 3.2.5 on 2022-07-15 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0025_auto_20220715_0900'),
        ('ruta', '0023_alter_planilla_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrecepcion',
            name='guia',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', related_query_name='recepcion', to='fisico.fisico'),
        ),
        migrations.AlterField(
            model_name='recepcion',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recepcion_guia', related_query_name='recepcion', to='fisico.fisico'),
        ),
    ]