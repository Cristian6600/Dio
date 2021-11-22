# Generated by Django 3.2.5 on 2021-11-16 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guia', '0002_guia_user'),
        ('courrier', '0001_initial'),
        ('datos_g', '0002_alter_datos_g_proceso'),
        ('fisico', '0003_alter_fisico_id_est'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Planilla')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha de entrega')),
                ('prueba', models.CharField(blank=True, max_length=30, null=True)),
                ('guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico')),
                ('mensajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier')),
            ],
            options={
                'verbose_name': 'Cargue',
                'verbose_name_plural': 'Cargue',
            },
        ),
        migrations.CreateModel(
            name='Lenguaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Lenguajes de Programacion',
                'verbose_name_plural': 'Lenguajes de Programacion',
            },
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.estado')),
                ('guia', models.ManyToManyField(to='fisico.Fisico')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_g.motivo')),
                ('planilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue')),
            ],
            options={
                'verbose_name': 'Recepcion',
                'verbose_name_plural': 'Recepciones',
            },
        ),
        migrations.CreateModel(
            name='Programador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('ocupation', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField(default=0)),
                ('languages', models.ManyToManyField(to='ruta.Lenguaje')),
            ],
            options={
                'verbose_name': 'Programador',
                'verbose_name_plural': 'Programadores',
                'ordering': ['full_name'],
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
                'ordering': ['-id'],
            },
        ),
    ]