from django.db import models
from applications.base_cliente.models import bd_clie
from simple_history.models import HistoricalRecords

       
class paquete(models.Model):

    bolsa = models.IntegerField(primary_key=True)
    Seudo = models.CharField(max_length=35)
    history = HistoricalRecords()

    unique_together = ('bolsa', 'Seudo')

    def __str__(self):
        return str(self.bolsa)

class Fisico (models.Model):

    Bolsa = models.IntegerField(primary_key=True, unique=True)
    Seudo = models.CharField(max_length=35)
    Fecha = models.DateTimeField(auto_now=True)
    Estado = models.BooleanField(default=True)
    
    
    class Meta:
        verbose_name = "Fisico"
        verbose_name_plural = "Fisico"
        unique_together = ('Bolsa', 'Seudo')

    def __str__(self):
        return str(self.Seudo)