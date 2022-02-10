# Generated by Django 3.2.5 on 2022-02-10 21:57

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bolsa',
            fields=[
                ('bolsa', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalFisico',
            fields=[
                ('bolsa_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='fisico.bolsa')),
                ('fecha', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha fisico')),
                ('estado', models.BooleanField(default=True)),
                ('bolsa', models.IntegerField(db_index=True)),
                ('id_guia', models.IntegerField(blank=True, db_index=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad Total')),
                ('suma', models.IntegerField(blank=True, default=0, null=True)),
                ('destinatario', models.CharField(blank=True, max_length=100, null=True)),
                ('d_i', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_recepcion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha gestion')),
                ('fecha_planilla', models.DateTimeField(blank=True, editable=False, null=True)),
                ('imagen', models.TextField(blank=True, max_length=100, null=True)),
                ('est_planilla', models.CharField(max_length=30)),
                ('id_planilla', models.IntegerField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical fisico',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'inconsistencias',
                'verbose_name_plural': 'inconsistencias',
            },
        ),
        migrations.CreateModel(
            name='Motivo_mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha fisico')),
                ('estado', models.BooleanField(default=True)),
                ('bolsa', models.IntegerField()),
                ('seudo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='base_cliente.bd_clie')),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('proceso', models.CharField(max_length=30)),
                ('cod_dir', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Fisico',
            fields=[
                ('bolsa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='fisico.bolsa')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha fisico')),
                ('estado', models.BooleanField(default=True)),
                ('id_guia', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad Total')),
                ('suma', models.IntegerField(blank=True, default=0, null=True)),
                ('destinatario', models.CharField(blank=True, max_length=100, null=True)),
                ('d_i', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_recepcion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha gestion')),
                ('fecha_planilla', models.DateTimeField(auto_now=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='guia')),
                ('est_planilla', models.CharField(max_length=30)),
                ('id_planilla', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('fisico.bolsa', models.Model),
        ),
    ]
