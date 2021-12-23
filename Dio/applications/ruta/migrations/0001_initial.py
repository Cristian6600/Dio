# Generated by Django 3.2.5 on 2021-12-23 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos_g', '0001_initial'),
        ('courrier', '0001_initial'),
        ('fisico', '0001_initial'),
        ('guia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Planilla')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha de entrega')),
                ('full_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier', verbose_name='Mensajero')),
            ],
            options={
                'verbose_name': 'Cargue',
                'verbose_name_plural': 'Cargue',
            },
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha recepcion')),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.estado')),
                ('guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_g.motivo')),
                ('planilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue')),
            ],
            options={
                'verbose_name': 'Recepcion',
                'verbose_name_plural': 'Recepciones',
            },
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue', verbose_name='Planilla')),
                ('guia', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico')),
            ],
            options={
                'ordering': ('guia__fecha', 'id'),
            },
        ),
        migrations.AddField(
            model_name='cargue',
            name='guia',
            field=models.ManyToManyField(blank=True, through='ruta.Planilla', to='fisico.Fisico'),
        ),
    ]
