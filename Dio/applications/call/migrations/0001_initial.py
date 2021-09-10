# Generated by Django 3.2.5 on 2021-09-06 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos_g', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('guia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='indicativo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.IntegerField(verbose_name='Indicativo')),
                ('Region', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historicaldatos_t',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('Activo', models.BooleanField(default=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('d_i', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='datos_g.datos_g')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('id_mot', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='guia.motivo')),
                ('indicativo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='call.indicativo')),
            ],
            options={
                'verbose_name': 'historical datos_t',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='datos_t',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('Activo', models.BooleanField(default=True)),
                ('d_i', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_g.datos_g')),
                ('id_mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guia.motivo')),
                ('indicativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.indicativo')),
            ],
        ),
    ]
