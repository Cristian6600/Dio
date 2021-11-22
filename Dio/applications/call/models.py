from django.db import models
from applications.datos_g.models import Motivo
from applications.users.models import User
from simple_history.models import HistoricalRecords

class Indicativo(models.Model):
    
    ind = models.IntegerField(
        verbose_name = 'Indicativo'
    )
    Region = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return str(self.ind)

class Datos_t(models.Model):
    
    # d_i = models.ForeignKey(datos_g,
    #     on_delete=models.CASCADE, 
    #     )

    telefono = models.IntegerField(blank=True, null=True)

    indicativo = models.ForeignKey(
        Indicativo, 
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
        )
    # id_mot = models.ForeignKey(
    #     Motivo, 
    #     on_delete=models.CASCADE
    #     )

    activo = models.BooleanField(
        default=True
    )
    history = HistoricalRecords()
    

    def __str__(self):
        return str(self.telefono)
    
