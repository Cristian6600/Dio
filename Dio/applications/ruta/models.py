from django.db import models

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

    mensajero = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE
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

    # def save(self, *args, **kwargs):
    #     self.guia.id_est_id = self.guia.id_est_id = 4

    #     self.guia.save()       
    #     super(Planilla, self).save(*args, **kwargs)

    # class Meta:
    #     ordering = ('guia__fecha', 'id')

class Recepcion(models.Model):

    planilla = models.ForeignKey(
        Cargue, 
        on_delete=models.CASCADE
    )

    motivo = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE
    )

    guia = models.ManyToManyField(
        Fisico, 
        
    )

    # bolsa = models.ForeignKey(Bolsa, on_delete=models.CASCADE, related_name='Bolsas', blank = True, null = True
    # )

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

    # @property
    # def varu(self):
    #   return self.motivo
        
    # def save(self, *args, **kwargs):

    #     # self.guia.mot = self.varu
    
    #     self.guia.save()

    #     super(Recepcion, self).save(*args, **kwargs)

# class Recep_guia(models.Model):

#     recepcions_id = models.AutoField(primary_key=True)

#     recepcion= models.ForeignKey(
#     'Recepcion',
#     on_delete=models.CASCADE, 
    
#     )

#     guiad = models.ForeignKey(
#     Fisico, 
#     on_delete=models.CASCADE,
    
#     )

#     def __str__(self):
#         return str(self.id)

    # @property
    # def estados(self):
    #     return self.estado

    # @property
    # def var(self):
    #   return self.motivo
    # contador = 0  
        
    # def save(self, *args, **kwargs):
    #     contador = 0
        # self.guia.mot  = self.var
    #     self.guia.id_est = self.estados
        # self.guia.id_est_id = self.guia.id_est_id = 3
        # self.guia.cantidad = self.guia.cantidad + 1
    #     # Funcion contador ok copiar codigo para pruebas
        # self.guia.suma = self.guia.suma
        # if self.guia.suma <=2:
        #     self.guia.suma +=1  # suma en campo sum en cada momento que se ejecute el boton de guardar
                      
        # self.guia.save()

        # super(Recep_guia,  self).save(*args, **kwargs)

from django.db import models


class Lenguaje(models.Model):
    
    languages = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Lenguajes de Programacion'
        verbose_name_plural = 'Lenguajes de Programacion'

    def __str__(self):
        return str(self.id) + ' ' + self.languages


class Programador(models.Model):

    full_name = models.CharField('Nombre', max_length=60)
    ocupation = models.CharField(max_length=50)
    age = models.PositiveIntegerField(default=0)
    languages = models.ManyToManyField(Lenguaje)

    class Meta:
        verbose_name='Programador'
        verbose_name_plural='Programadores'
        ordering=['full_name']

    def __str__(self):
        return str(self.id) + ' ' + self.full_name

