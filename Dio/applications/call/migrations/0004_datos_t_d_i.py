# Generated by Django 3.2.5 on 2021-07-26 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0004_alter_guia_imagen'),
        ('call', '0003_auto_20210726_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_t',
            name='d_i',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='guia.guia'),
            preserve_default=False,
        ),
    ]