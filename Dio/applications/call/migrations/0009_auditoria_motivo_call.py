# Generated by Django 3.2.5 on 2022-05-16 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argumento', '0002_motivo_call'),
        ('call', '0008_auditoria_estado_llamada'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditoria',
            name='motivo_call',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='argumento.motivo_call'),
            preserve_default=False,
        ),
    ]
