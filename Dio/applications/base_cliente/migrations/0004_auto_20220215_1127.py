# Generated by Django 3.2.5 on 2022-02-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('argumento', '0004_est_clie'),
        ('base_cliente', '0003_auto_20220215_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bd_clie',
            name='id_est_clie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='argumento.est_clie', verbose_name='Id estado cliente '),
        ),
        migrations.DeleteModel(
            name='Est_clie',
        ),
    ]