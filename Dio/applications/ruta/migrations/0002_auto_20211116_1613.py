# Generated by Django 3.2.5 on 2021-11-16 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fisico', '0003_alter_fisico_id_est'),
        ('courrier', '0001_initial'),
        ('ruta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargue',
            options={},
        ),
        migrations.AlterModelOptions(
            name='planilla',
            options={'verbose_name': 'Cargue', 'verbose_name_plural': 'Cargue'},
        ),
        migrations.RemoveField(
            model_name='cargue',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='cargue',
            name='guia',
        ),
        migrations.RemoveField(
            model_name='cargue',
            name='mensajero',
        ),
        migrations.RemoveField(
            model_name='cargue',
            name='prueba',
        ),
        migrations.RemoveField(
            model_name='planilla',
            name='cargue',
        ),
        migrations.AddField(
            model_name='planilla',
            name='fecha',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de entrega'),
        ),
        migrations.AddField(
            model_name='planilla',
            name='mensajero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planilla',
            name='planilla',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='plan', to='ruta.planilla'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planilla',
            name='prueba',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='cargue',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='Planillas'),
        ),
        migrations.AlterField(
            model_name='planilla',
            name='guia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fisico.fisico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recepcion',
            name='planilla',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planillas', to='ruta.cargue'),
        ),
    ]
