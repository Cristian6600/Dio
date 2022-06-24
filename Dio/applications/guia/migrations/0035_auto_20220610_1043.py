# Generated by Django 3.2.5 on 2022-06-10 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0034_remove_img_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoberturaPdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='pdf_cobertura')),
            ],
        ),
        migrations.AlterField(
            model_name='historicalguia',
            name='estado_img',
            field=models.CharField(blank=True, choices=[('ENTREGA', 'ENTREGA'), ('ENTREGA_DIGITALIZADA', 'ENTREGA DIGITALIZADA')], max_length=22, null=True, verbose_name='gestion'),
        ),
    ]