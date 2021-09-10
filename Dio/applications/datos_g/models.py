from django.db import models

from applications.cliente.models import Ciudad

from applications.base_cliente.models import Producto
from django.dispatch import receiver
from django.db.models.signals import post_save
from applications.base_cliente.models import bd_clie



class datos_g (models.Model):

    id = models.OneToOneField(
        bd_clie,
        primary_key = True,
        on_delete=models.CASCADE,
        help_text = 'Codigo de barras',
        unique = True,
        verbose_name = 'seudo'
    )

    bolsa = models.IntegerField(
        
        help_text = 'Codigo de barras'
    )
    fecha = models.DateTimeField(auto_now_add=True,
        verbose_name = 'Fecha fisico')

    d_i = models.BigIntegerField(
        blank=True, 
        null=True,
        verbose_name = 'Documento de identidad'
    )
    
    direccion = models.CharField(
        max_length= 255,
        blank=True, 
        null=True,
    )

    # dest = models.CharField(
    #     max_length=100
    # )

    postal = models.CharField(
        max_length = 7,
        blank=True, 
        null=True,
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad',
        null=True,
        blank=True,
        
    )
    barrio = models.CharField(
        max_length = 70,
        null=True,
        blank=True,
    )  
    marca = models.CharField(
        max_length= 15,
        null=True, 
        blank = True
    )  
    id_pro = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )

    gx = models.BigIntegerField(
        null=True,
        blank=True,
    )
    gy = models.BigIntegerField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Datos de gestion"
        verbose_name_plural = "Datos de gestion"

    @property
    def var(self):
      return (self.fecha)

    def save(self, *args, **kwargs):
        self.id.fe_fisico  = self.var
        
        self.id.save()

        super(datos_g, self).save(*args, **kwargs)
              
    def __str__(self):
        return str(self.id)
    




    