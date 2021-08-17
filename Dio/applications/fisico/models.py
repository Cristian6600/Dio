from django.db import models
from applications.base_cliente.models import bd_clie


from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError


       
class paquete(models.Model):

    bolsa = models.IntegerField(
        unique = True,
        help_text = 'Codigo de barras'
    )

    Seudo = models.ForeignKey(
        bd_clie,
        on_delete=models.CASCADE, 
        help_text = 'Codigo de barras',
        unique = True
    )

    
    Fecha = models.DateTimeField(auto_now=True)
    Estado = models.BooleanField(default=True)

    unique_together = ('bolsa', 'Seudo')

    @property
    def var(self):
      return (self.bolsa)

    def save(self, *args, **kwargs):
        self.Seudo.Bolsa  = self.var
        
        self.Seudo.save()

        super(paquete, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.bolsa) 


    
    