# Generated by Django 3.2.5 on 2022-02-16 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fisico', '0002_initial'),
        ('courrier', '0001_initial'),
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Gestion'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='cargue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue', verbose_name='Planilla'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='full_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier', verbose_name='Mensajero'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='guia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planilla_filtro', to='fisico.fisico'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario Gestion'),
        ),
        migrations.AddField(
            model_name='cargue',
            name='full_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier', verbose_name='Mensajero'),
        ),
        migrations.AddField(
            model_name='cargue',
            name='guia',
            field=models.ManyToManyField(through='ruta.Planilla', to='fisico.Fisico'),
        ),
    ]
