# Generated by Django 3.2.5 on 2022-02-11 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courrier', '0002_modelo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehiculo',
            name='modelo',
        ),
        migrations.AddField(
            model_name='vehiculo',
            name='modelos',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='courrier.modelo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='modelo',
            name='modelo',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
