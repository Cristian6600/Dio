from django.db import models

from applications.cliente.models import Ciudad
from applications.guia.models import Motivo

class datos_g (models.Model):
    Seudo = models.CharField(
        max_length = 35
    )
    direccion = models.CharField(
        max_length= 255
    )
    postal = models.CharField(
        max_length = 7
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad'
    )
    barrio = models.CharField(
        max_length = 70,
        null=True,
        blank=True,
    )    
    id_mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name = 'Id motivo',
    )

    gx = models.BigIntegerField(
        null=True,
        blank=True,
    )
    gy = models.BigIntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Datos de gestion"
        verbose_name_plural = "Datos de gestion"

    def __str__(self):
        return self.Seudo