# Generated by Django 3.2.5 on 2022-02-10 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0002_initial'),
        ('guia', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalguia',
            name='mot',
            field=models.ForeignKey(blank=True, db_constraint=False, default=4, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='datos_g.motivo', verbose_name='motivo'),
        ),
    ]