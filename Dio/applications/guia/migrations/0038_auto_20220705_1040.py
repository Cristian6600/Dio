# Generated by Django 3.2.5 on 2022-07-05 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0037_alter_historicalguia_id_est'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guia',
            options={'verbose_name': 'Buscar', 'verbose_name_plural': 'Guia'},
        ),
        migrations.AlterModelOptions(
            name='historicalguia',
            options={'get_latest_by': 'history_date', 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical Buscar'},
        ),
    ]
