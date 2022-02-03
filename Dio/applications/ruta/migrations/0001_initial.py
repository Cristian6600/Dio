# Generated by Django 3.2.5 on 2022-02-03 14:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('guia', '0001_initial'),
        ('fisico', '0001_initial'),
        ('datos_g', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargue',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Planilla')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha de entrega')),
            ],
            options={
                'verbose_name': 'Cargue',
                'verbose_name_plural': 'Cargue',
            },
        ),
        migrations.CreateModel(
            name='Est_planilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Planilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('cont', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True, verbose_name='Fecha recepcion')),
                ('estado', models.ForeignKey(blank=True, default=3, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.estado')),
                ('guia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico')),
                ('motivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos_g.motivo')),
            ],
            options={
                'verbose_name': 'Recepcion',
                'verbose_name_plural': 'Recepciones',
            },
        ),
    ]
