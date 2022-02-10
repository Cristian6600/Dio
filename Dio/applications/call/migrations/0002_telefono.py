# Generated by Django 3.2.5 on 2022-02-10 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('call', '0001_initial'),
        ('guia', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.OneToOneField(max_length=12, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='guia.guia')),
                ('tel', models.CharField(max_length=80)),
                ('indicativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='call.indicativo')),
            ],
        ),
    ]
