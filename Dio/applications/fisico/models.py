from django.db import models
from applications.base_cliente.models import bd_clie
from simple_history.models import HistoricalRecords
from applications.guia.models import guia

       
class paquete(models.Model):

    bolsa = models.ForeignKey(
        guia, 
        on_delete=models.CASCADE
    )
    Seudo = models.CharField(
        max_length=35, 
        unique = True
    )
    Fecha = models.DateTimeField(auto_now=True)
    Estado = models.BooleanField(default=True)

    unique_together = ('bolsa', 'Seudo')

    def __str__(self):
        return str(self.bolsa) 


    
    