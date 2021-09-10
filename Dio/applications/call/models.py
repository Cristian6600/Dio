from django.db import models
from applications.guia.models import Motivo
from applications.datos_g.models import datos_g
from simple_history.models import HistoricalRecords

class indicativo(models.Model):
    
    ind = models.IntegerField(
        verbose_name = 'Indicativo'
    )
    Region = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return str(self.ind)

class datos_t(models.Model):
    

    d_i = models.ForeignKey(datos_g,
        on_delete=models.CASCADE, 
        )

    telefono = models.IntegerField()

    indicativo = models.ForeignKey(
        indicativo, 
        on_delete=models.CASCADE,
    )

    id_mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE
        )

    Activo = models.BooleanField(
        default=True
    )
    history = HistoricalRecords()
    

    def __str__(self):
        return str(self.telefono)
    

    

    
    