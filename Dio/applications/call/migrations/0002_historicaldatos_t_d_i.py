# Generated by Django 3.2.5 on 2021-12-21 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos_g', '0001_initial'),
        ('call', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldatos_t',
            name='d_i',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='datos_g.datos_g', verbose_name='Seudo buscar'),
        ),
    ]
