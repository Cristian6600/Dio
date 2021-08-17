from django.db import models

from applications.cliente.models import Ciudad
from applications.guia.models import guia
from applications.base_cliente.models import Producto
from applications.guia.models import Motivo

class datos_g (models.Model):
    Seudo = models.ForeignKey(
        guia, on_delete=models.CASCADE,
        max_length = 35
    )
    
    direccion = models.CharField(
        max_length= 255
    )

    d_i = models.BigIntegerField(
        blank=True, 
        null=True,
        verbose_name = 'Documento de identidad'
    )
    postal = models.CharField(
        max_length = 7
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad'
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
        on_delete=models.CASCADE
    )
    id_mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name = 'Id motivo',
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
    def vard(self):
      return (self.direccion)

    def save(self, *args, **kwargs):
        self.Seudo.Direccion  = self.vard
        print('========Holas=============')
        self.Seudo.save()

        super(datos_g, self).save(*args, **kwargs)

    @property
    def var(self):
      return (self.d_i)

    def save(self, *args, **kwargs):
        self.Seudo.d_i  = self.var
        print('========Holas=============')
        self.Seudo.save()

        super(datos_g, self).save(*args, **kwargs)

    # @property
    # def varm(self):
    #   return (self.marca)

    # def save(self, *args, **kwargs):
    #     self.Seudo.marca  = self.varm
    #     print('========Holas=============')
    #     self.Seudo.save()

    #     super(datos_g, self).save(*args, **kwargs)

    # @property
    # def varpro(self):
    #   return (self.marca)

    # def save(self, *args, **kwargs):
    #     self.Seudo.marca  = self.varpro
    #     print('========Holas=============')
    #     self.Seudo.save()

    #     super(datos_g, self).save(*args, **kwargs)

        

    def __str__(self):
        return str(self.Seudo)