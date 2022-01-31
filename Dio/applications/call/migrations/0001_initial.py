# Generated by Django 3.2.5 on 2022-01-31 22:52

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion_5', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=2)),
                ('observacion', models.CharField(max_length=30)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calficacion', models.CharField(max_length=22)),
            ],
        ),
        migrations.CreateModel(
            name='Datos_t',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Gestion',
                'verbose_name_plural': 'Gestion',
            },
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
            ],
            options={
                'verbose_name': 'historical Gestion',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
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
    ]
