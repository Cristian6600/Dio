# Generated by Django 3.2.5 on 2022-07-08 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0001_initial'),
        ('fisico', '0023_auto_20220629_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fisico',
            name='mensajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_guia', to='courrier.courrier'),
        ),
    ]
