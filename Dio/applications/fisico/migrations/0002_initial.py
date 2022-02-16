# Generated by Django 3.2.5 on 2022-02-15 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courrier', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cliente', '0001_initial'),
        ('argumento', '0001_initial'),
        ('fisico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paquete',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='mesa',
            name='id_motivo_m',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.motivo_mesa', verbose_name='motivo'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='cod_vis',
            field=models.ForeignKey(blank=True, db_constraint=False, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.cod_vis'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='id_ciu',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='cliente.ciudad', verbose_name='ciudad'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='id_est',
            field=models.ForeignKey(blank=True, db_constraint=False, default=4, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='mensajero',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='courrier.courrier'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='mot',
            field=models.ForeignKey(blank=True, db_constraint=False, default=4, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.motivo', verbose_name='motivo'),
        ),
        migrations.AddField(
            model_name='historicalfisico',
            name='proceso',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='argumento.proceso'),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='id_est',
            field=models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='bolsa',
            name='mot',
            field=models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.motivo', verbose_name='motivo'),
        ),
        migrations.AlterUniqueTogether(
            name='paquete',
            unique_together={('bolsa', 'seudo')},
        ),
        migrations.AddField(
            model_name='mesa',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='cod_vis',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.cod_vis'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='id_ciu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='ciudad'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='mensajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier'),
        ),
        migrations.AddField(
            model_name='fisico',
            name='proceso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.proceso'),
        ),
        migrations.AddField(
            model_name='cobertura',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
