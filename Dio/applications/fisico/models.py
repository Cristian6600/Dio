from django.db import models
from applications.base_cliente.models import bd_clie


from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
       
class paquete(models.Model):

    seudo = models.OneToOneField(
        bd_clie,
        primary_key = True,
        on_delete=models.CASCADE,
        help_text = 'Codigo de barras',
        unique = True
    )

    bolsa = models.IntegerField(
        
        help_text = 'Codigo de barras'
    )

    fecha = models.DateTimeField(
        auto_now=True
    )
    estado = models.BooleanField(
        default=True
    )

    unique_together = ('bolsa', 'seudo')

    @property
    def var(self):
      return (self.bolsa)

    def save(self, *args, **kwargs):
        self.seudo.bolsa  = self.var
        
        self.seudo.save()

        super(paquete, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.bolsa) 


    
    