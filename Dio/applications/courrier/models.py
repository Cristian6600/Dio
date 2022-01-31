from django.db import models

from applications.cliente.models import Ciudad
from .managers import CourrierManager

class vehiculo(models.Model):

    id_veg = models.IntegerField(primary_key=True, verbose_name = 'Id vehiculo')

    vehiculo = models.CharField(max_length=35)

    marca = models.CharField(max_length=20)

    cilindraje = models.IntegerField()

    capacidad = models.IntegerField()

    class Meta:
        verbose_name = "Vehiculo"
        verbose_name_plural = "Vehiculo"

    def __str__(self):
        return str(self.id_veg)

class courrier(models.Model):

    id_courrier = models.IntegerField(
        verbose_name = 'Id Courrier'
    )
    d_i = models.BigIntegerField()

    courrier = models.CharField(
        max_length=70, 
        verbose_name = 'Nombre courrier'
    )
    cel = models.PositiveBigIntegerField(
        verbose_name = 'Celular'
    )
    dir = models.CharField(
        max_length=120
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad'
    )

    id_veh = models.IntegerField(
        verbose_name = 'Id vehiculo'
    )

    placa = models.CharField(
        max_length = 6
    )

    soat = models.CharField(
        max_length = 25
    )

    tecnomecanica = models.BooleanField(
        default=False
    )

    infraccion = models.IntegerField()

    modelo = models.DateField()

    licencia = models.IntegerField()

    objects = CourrierManager()

    class Meta:
        verbose_name = "Courrier"
        verbose_name_plural = "Courrier"

    def __str__(self):
        return self.courrier


