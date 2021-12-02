# Generated by Django 3.2.5 on 2021-12-02 17:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guia', '0002_initial'),
        ('datos_g', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calficacion', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Indicativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.IntegerField(verbose_name='Indicativo')),
                ('Region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('cc', models.CharField(max_length=15)),
                ('tel', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('indicativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.indicativo')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalDatos_t',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('d_i', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='datos_g.datos_g', verbose_name='Seudo buscar')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('telefono', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='call.telefono')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'historical Gestion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Datos_t',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('d_i', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_g.datos_g', verbose_name='Seudo buscar')),
                ('telefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.telefono')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Gestion',
                'verbose_name_plural': 'Gestion',
            },
        ),
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion_5', models.CharField(max_length=2)),
                ('observacion', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('calificacion_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_1', to='call.calificacion')),
                ('calificacion_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_2', to='call.calificacion')),
                ('calificacion_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_3', to='call.calificacion')),
                ('calificacion_4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion_4', to='call.calificacion')),
                ('entregas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.guia')),
                ('pregunta_1', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='call.pregunta')),
                ('pregunta_2', models.ForeignKey(blank=True, default=2, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_2', to='call.pregunta')),
                ('pregunta_3', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_3', to='call.pregunta')),
                ('pregunta_4', models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_4', to='call.pregunta')),
                ('pregunta_5', models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta_5', to='call.pregunta')),
                ('telefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.telefono')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
    ]
