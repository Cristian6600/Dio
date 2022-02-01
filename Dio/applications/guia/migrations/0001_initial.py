# Generated by Django 3.2.5 on 2022-02-01 15:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base_cliente', '0001_initial'),
        ('fisico', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cod_vis',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='Codigo de visita')),
                ('visita', models.CharField(max_length=36)),
                ('tipo', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Estado', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('fisico_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='fisico.fisico')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('seudo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='guias', serialize=False, to='base_cliente.bd_clie')),
                ('postal', models.CharField(blank=True, max_length=7, null=True)),
                ('barrio', models.CharField(blank=True, max_length=70, null=True)),
                ('m', models.IntegerField(blank=True, default=1, null=True)),
                ('ancho', models.IntegerField(blank=True, default=1, null=True)),
                ('alto', models.IntegerField(blank=True, default=1, null=True)),
                ('largo', models.IntegerField(blank=True, default=1, null=True)),
                ('copia', models.IntegerField(blank=True, default=1, null=True)),
                ('unidad', models.IntegerField(blank=True, default=1, null=True)),
                ('contiene', models.CharField(blank=True, max_length=50, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('domicilio', models.IntegerField(blank=True, default=0, null=True)),
                ('acarreo', models.IntegerField(blank=True, default=0, null=True)),
                ('flete', models.IntegerField(blank=True, default=0, null=True)),
                ('declarado', models.IntegerField(blank=True, default=0, null=True)),
                ('cantidad_vi', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cantidad visitas')),
                ('codigo', models.CharField(blank=True, max_length=28, null=True)),
                ('or_imp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Guia',
                'verbose_name_plural': 'Guia',
            },
            bases=('fisico.fisico', models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGuia',
            fields=[
                ('fisico_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='fisico.fisico')),
                ('bolsa_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='fisico.bolsa')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha', models.DateTimeField(blank=True, editable=False)),
                ('estado', models.BooleanField(default=True)),
                ('bolsa', models.IntegerField(db_index=True)),
                ('id_guia', models.IntegerField(blank=True, db_index=True)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('cantidad', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Cantidad Total')),
                ('suma', models.IntegerField(blank=True, default=0, null=True)),
                ('destinatario', models.CharField(blank=True, max_length=100, null=True)),
                ('d_i', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha_recepcion', models.DateTimeField(blank=True, null=True)),
                ('fecha_planilla', models.DateTimeField(blank=True, null=True)),
                ('imagen', models.TextField(blank=True, max_length=100, null=True)),
                ('est_planilla', models.CharField(max_length=30)),
                ('id_planilla', models.IntegerField(blank=True, null=True)),
                ('postal', models.CharField(blank=True, max_length=7, null=True)),
                ('barrio', models.CharField(blank=True, max_length=70, null=True)),
                ('m', models.IntegerField(blank=True, default=1, null=True)),
                ('ancho', models.IntegerField(blank=True, default=1, null=True)),
                ('alto', models.IntegerField(blank=True, default=1, null=True)),
                ('largo', models.IntegerField(blank=True, default=1, null=True)),
                ('copia', models.IntegerField(blank=True, default=1, null=True)),
                ('unidad', models.IntegerField(blank=True, default=1, null=True)),
                ('contiene', models.CharField(blank=True, max_length=50, null=True)),
                ('orden', models.IntegerField(blank=True, null=True)),
                ('domicilio', models.IntegerField(blank=True, default=0, null=True)),
                ('acarreo', models.IntegerField(blank=True, default=0, null=True)),
                ('flete', models.IntegerField(blank=True, default=0, null=True)),
                ('declarado', models.IntegerField(blank=True, default=0, null=True)),
                ('cantidad_vi', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cantidad visitas')),
                ('codigo', models.CharField(blank=True, max_length=28, null=True)),
                ('or_imp', models.IntegerField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical Guia',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id_serv', models.IntegerField(primary_key=True, serialize=False)),
                ('Servicio', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicio',
            },
        ),
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='guia')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('numero', models.CharField(blank=True, max_length=30, null=True)),
                ('id_guia', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico')),
            ],
            options={
                'verbose_name': 'Imagenes Guia',
                'verbose_name_plural': 'Imagenes Guia',
            },
        ),
    ]
