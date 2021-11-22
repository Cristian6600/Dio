# Generated by Django 3.2.5 on 2021-11-17 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0003_alter_fisico_id_est'),
        ('courrier', '0001_initial'),
        ('ruta', '0004_auto_20211116_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargue',
            name='planilla',
        ),
        migrations.RemoveField(
            model_name='planilla',
            name='mensajero',
        ),
        migrations.AddField(
            model_name='cargue',
            name='mensajero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planilla',
            name='cargue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue', verbose_name='Planilla'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='guia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
        ),
        migrations.RemoveField(
            model_name='cargue',
            name='guia',
        ),
        migrations.AddField(
            model_name='cargue',
            name='guia',
            field=models.ManyToManyField(blank=True, through='ruta.Planilla', to='fisico.Fisico'),
        ),
        migrations.AlterField(
            model_name='cargue',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Planilla'),
        ),
        migrations.AlterField(
            model_name='recepcion',
            name='planilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ruta.cargue'),
        ),
    ]
