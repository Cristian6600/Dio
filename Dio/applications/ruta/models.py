from django.db import models

from applications.guia.models import guia, Motivo
from applications.courrier.models import courrier

class Cargue(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name ='Planilla',
    )
    guia = models.ManyToManyField(
        guia, 
        
    )

    mensajero = models.OneToOneField(
        courrier, 
        on_delete=models.CASCADE
        )
    # motivo = models.ForeignKey(
    #     Motivo, 
    #     on_delete=models.CASCADE
    # )

    fecha = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.id)

class Recepcion(models.Model):

    planilla = models.OneToOneField(
        Cargue, on_delete=models.CASCADE
    )

    motivo = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE
    )

    guia = models.ForeignKey(
        guia, 
        on_delete=models.CASCADE
    )

    bolsa = models.PositiveIntegerField(
        blank=True, 
        null=True, 
    )

    fecha = models.DateTimeField(
        auto_now=True 
    )

    @property
    def var(self):
      return (self.motivo)

    def save(self, *args, **kwargs):
        self.guia.id_mot  = self.var
        self.guia.cantidad = self.guia.cantidad + 1
        
        self.guia.save()

        super(Recepcion, self).save(*args, **kwargs)

    
    def __str__(self):
        return str(self.planilla)