# Generated by Django 3.2.5 on 2022-01-17 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('call', '0002_historicaldatos_t_d_i'),
        ('guia', '0001_initial'),
        ('datos_g', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicaldatos_t',
            name='history_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='historicaldatos_t',
            name='telefono',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='call.telefono'),
        ),
        migrations.AddField(
            model_name='historicaldatos_t',
            name='user',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='datos_t',
            name='d_i',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_g.datos_g', verbose_name='Seudo buscar'),
        ),
        migrations.AddField(
            model_name='datos_t',
            name='telefono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.telefono'),
        ),
        migrations.AddField(
            model_name='datos_t',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_1', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_2', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_3', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='calificacion_4',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_4', to='call.calificacion'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='entregas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.guia'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='pregunta_1',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='call.pregunta'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='pregunta_2',
            field=models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_2', to='call.pregunta'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='pregunta_3',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_3', to='call.pregunta'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='pregunta_4',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_4', to='call.pregunta'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='pregunta_5',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_5', to='call.pregunta'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='telefono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.telefono'),
        ),
        migrations.AddField(
            model_name='auditoria',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
