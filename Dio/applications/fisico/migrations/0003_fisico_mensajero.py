# Generated by Django 3.2.5 on 2022-01-18 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0001_initial'),
        ('fisico', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fisico',
            name='mensajero',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courrier.courrier'),
        ),
    ]
