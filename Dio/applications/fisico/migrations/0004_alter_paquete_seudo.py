# Generated by Django 3.2.5 on 2021-08-12 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base_cliente', '0001_initial'),
        ('fisico', '0003_remove_paquete_seudo_pa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paquete',
            name='Seudo',
            field=models.ForeignKey(help_text='Codigo de barras', on_delete=django.db.models.deletion.CASCADE, to='base_cliente.bd_clie'),
        ),
    ]
