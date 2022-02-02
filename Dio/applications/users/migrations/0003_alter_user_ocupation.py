# Generated by Django 3.2.5 on 2022-02-02 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_ocupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ocupation',
            field=models.CharField(blank=True, choices=[('0', 'Custodia'), ('1', 'Mesa'), ('2', 'Call'), ('3', 'Courrier'), ('4', 'Sig'), ('5', 'Tecnologia')], max_length=1),
        ),
    ]
