# Generated by Django 3.2.5 on 2021-11-30 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datos_g', '0002_initial'),
        ('call', '0003_auditoria_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_t',
            name='d_i',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='datos_g.datos_g'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaldatos_t',
            name='d_i',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='datos_g.datos_g'),
        ),
    ]
