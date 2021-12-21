from django.db import models

from django.urls import reverse
from applications.guia.models import  Estado
from applications.courrier.models import courrier
from applications.datos_g.models import Motivo
from applications.fisico.models import Fisico, Bolsa
from applications.guia.models import Guia
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple

class Cargue(models.Model):

    id = models.AutoField(
        primary_key=True,
        verbose_name ='Planilla',
    )
    guia = models.ManyToManyField(
        Fisico, 
        through= 'Planilla', 
        blank = True, 
           
    )

    full_name = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, blank=True, null=True
        )

    fecha = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de entrega')
    
    class Meta: 
        verbose_name = "Cargue"
        verbose_name_plural = "Cargue"

    def __str__(self):
        return str(self.id)

    def myfunc(self):
        print(self.id)

class Planilla(models.Model) :
    guia = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE, blank = True, null = True
    )
    cargue = models.ForeignKey(
        Cargue, 
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name="Planilla"
    )
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        self.guia.id_est_id = self.guia.id_est_id = 4

        self.guia.save()       
        super(Planilla, self).save(*args, **kwargs)

    class Meta:
        ordering = ('guia__fecha', 'id')

class Recepcion(models.Model):

    planilla = models.ForeignKey(
        Cargue, 
        on_delete=models.CASCADE
    )

    motivo = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE
    )

    guia = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE
        
    )

    fecha = models.DateTimeField(
        auto_now=True 
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        blank=True, 
        null=True, 
    )

    class Meta:
        verbose_name = "Recepcion"
        verbose_name_plural = "Recepciones"

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('Recepcion:detail', args=[self.id])

    @property
    def varu(self):
      return self.motivo

    @property
    def estados(self):
        return self.estado
        
    def save(self, *args, **kwargs):

        self.guia.mot_id = self.varu
        self.guia.id_est = self.estados
    
        self.guia.save()

        super(Recepcion, self).save(*args, **kwargs)

