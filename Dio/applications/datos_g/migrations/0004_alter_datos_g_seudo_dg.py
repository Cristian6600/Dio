# Generated by Django 3.2.5 on 2022-01-12 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0002_initial'),
        ('datos_g', '0003_auto_20220112_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_g',
            name='seudo_dg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='guia.guia'),
        ),
    ]