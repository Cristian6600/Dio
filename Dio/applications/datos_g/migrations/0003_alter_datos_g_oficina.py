# Generated by Django 3.2.5 on 2022-02-22 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
        ('datos_g', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_g',
            name='oficina',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cliente.oficinas'),
        ),
    ]
