# Generated by Django 3.2.5 on 2021-12-02 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='Dane')),
                ('ciudad', models.CharField(max_length=80)),
                ('cubrimiento', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudad',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departamento', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_clie', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id cliente')),
                ('nit', models.CharField(max_length=20)),
                ('r_s', models.CharField(max_length=70, verbose_name='Razon social')),
                ('contact', models.CharField(max_length=50, verbose_name='Contacto')),
                ('dir', models.CharField(max_length=120, verbose_name='Direccion')),
                ('tel', models.IntegerField(verbose_name='Tel fijo')),
                ('cel', models.IntegerField(verbose_name='Celular')),
                ('ind', models.IntegerField(verbose_name='Indicativo')),
                ('radicacion', models.IntegerField()),
                ('fact', models.CharField(max_length=4, verbose_name='Factura')),
                ('id_ciu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.ciudad', verbose_name='Id ciudad')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Cliente',
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.departamento', verbose_name='Departamento'),
        ),
    ]
