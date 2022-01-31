from django.db import models
from django.forms.widgets import NumberInput

from  django.db.models.signals import post_save

from django.conf import settings 

from django.urls import reverse
from applications.guia.models import  Estado
from applications.courrier.models import courrier
from applications.datos_g.models import Motivo
from applications.fisico.models import Fisico, Bolsa
from applications.guia.models import Guia
from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from model_utils.models import TimeStampedModel
from .managers import ProductManager

class Est_planilla(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.estado)

class Cargue(TimeStampedModel):

    id = models.AutoField(
        primary_key=True,
        verbose_name ='Planilla',
    )
    guia = models.ManyToManyField(
        Fisico, 
        through= 'Planilla', 
  
    )

    full_name = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, 
        verbose_name= 'Mensajero'
        )

    fecha = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de entrega')

    objects = ProductManager()

     
    class Meta: 
        verbose_name = "Cargue"
        verbose_name_plural = "Cargue"

    def __str__(self):
        return str(self.id)
  
class Planilla(TimeStampedModel) :

    guia = models.ForeignKey(
        Fisico, 
        related_name= "planilla_filtro",
        on_delete=models.CASCADE
    )
    cargue = models.ForeignKey(
        Cargue, 
        on_delete=models.CASCADE,
        blank=True, null=True,
        verbose_name="Planilla"
    )
    full_name = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, 
        verbose_name= 'Mensajero',
        blank = True, null= True
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario Gestion',
    )

    fecha = models.DateTimeField(
        auto_now=True
    )
    cont = models.IntegerField(blank=True, null=True)
    
    def authenticated(self, user):
        return self.filter(user=user)

    def __str__(self):
        return str(self.guia)

    @property
    def cargues(self):
        return str(self.cargue)

    @property
    def mensajero(self):
        return self.full_name

    @property
    def id_planilla(self):
        return self.id

    @property
    def contar(self):
        return self.cont

    @property
    def fecha_planilla(self):
        return self.fecha

#f
    def save(self, *args, **kwargs):
        
        self.guia.id_est_id = self.guia.id_est_id = 4
        self.guia.mensajero = self.mensajero
        self.guia.est_planilla = self.guia.est_planilla = 1
        self.guia.id_planilla = self.id_planilla     
        self.guia.fecha_planilla   = self.fecha_planilla

        self.guia.save()       
        super(Planilla,  self).save(*args, **kwargs)

class Recepcion(models.Model):

    motivo = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE
    )

    guia = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE
        
    )

    fecha = models.DateTimeField(
        auto_now=True,
        verbose_name = 'Fecha recepcion'
    )

    estado = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE,
        blank=True, 
        null=True, 
        default = 3
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario Gestion',
    )

    class Meta:
        verbose_name = "Recepcion"
        verbose_name_plural = "Recepciones"

    def __str__(self):
        return str(self.id)

    @property
    def varu(self):
      return self.motivo.id

    @property
    def estados(self):
        return self.estado
        
    def save(self, *args, **kwargs):
    
        self.guia.mot_id = self.varu
        self.guia.id_est = self.estados
        self.guia.est_planilla = self.guia.est_planilla =  2
        print (self.varu)
        self.guia.save()

        super(Recepcion, self).save(*args, **kwargs)



