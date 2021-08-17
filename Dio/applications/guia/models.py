from django.db import models
from applications.cliente.models import Cliente
from applications.fisico.models import paquete
from applications.base_cliente.models import bd_clie, Producto
from applications.users.models import User
from django.db.models.signals import post_save
from PIL import Image
from .managers import ProductManager

class tipo(models.Model):
    id_tip = models.IntegerField(
        primary_key=True
    )

    Tipo = models.CharField(
        max_length=20
    )

    class Meta:
        verbose_name = "Tipo"
        verbose_name_plural = "Tipo"

    def __str__(self):
        return str(self.Tipo)

class Estado (models.Model):
    id_est = models.IntegerField(
        primary_key = True
    )
    Estado = models.CharField(
        max_length=35
    )

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estado"

    def __str__(self):
        return str(self.Estado)

class Motivo(models.Model):

    Id_mot = models.IntegerField()

    Motivo = models.CharField(
        max_length=50
    )

    id_tip = models.ForeignKey(
        tipo, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.Motivo)

    class Meta:
        verbose_name = "Motivo"
        verbose_name_plural = "Motivo"

class Servicio(models.Model):
    id_serv = models.IntegerField(
        primary_key = True
    )
    Servicio = models.CharField(
        max_length=25
    )

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicio"

    def __str__(self):
        return str(self.id_serv) + '-' + self.Servicio
    
class guia(paquete):

    g = models.AutoField(
        primary_key = True,
        null=False,
        unique=True,
        verbose_name = 'Guia'
    )

    Direccion = models.CharField(
        max_length=255,
        blank = True,
        null = True
    )

    Estados = models.BooleanField(
        default=True
    )

    id_ser = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Servicio'
        
    )
    id_clie = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Cliente'
        
    )
    d_i = models.BigIntegerField(
        blank=True, 
        null=True,
        verbose_name = 'Documento de identidad'
    )
        
    m = models.IntegerField(
        default=1, 
        null=True, 
        blank = True
    )
    Ancho = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    Alto = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    Largo = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    Copia = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    Unidad = models.IntegerField(
        default=1, 
        null=True, 
        blank = True
    )
    Contiene = models.CharField(
        max_length = 50, 
        null=True, 
        blank = True
    )
    Orden = models.IntegerField(
        null=True, 
        blank = True
    )

    Domicilio = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    Acarreo = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    Flete = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    Declarado = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
     
    id_mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE, 
        verbose_name= 'Motivo', 
        null=True, 
        blank = True
    )

    Imagen = models.ImageField(
        upload_to = 'guia',
        null=True, 
        blank = True,
        
    )

    id_est = models.ForeignKey(
        Estado,
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Estado'
    )

    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True
    )

    marca = models.CharField(
        max_length= 15,
        null=True, 
        blank = True
    )

    objects = ProductManager()

    @property
    def varg(self):
      return 'guia/' + str(self.g) + '.jpg'

    def save(self, *args, **kwargs):
        self.Imagen  = self.varg
        super (guia, self).save()
     
    class Meta:
        verbose_name = "guia"
        verbose_name_plural = "guia"
        order_with_respect_to = 'id_mot'
   
    def __str__(self):
        return str(self.g  )    

    # @property
    # def varg(self):
    #   return (self.g)

    # def save(self, *args, **kwargs):
    #     self.Seudo.guia  = self.varg
    #     print('========Holas=============')
    #     self.Seudo.save()

    #     super(guia, self).save(*args, **kwargs)

    
    # def optimize_image(sender, instance, **kwargs):
    #     print("==========")
    #     print(instance)
    #     if instance.Imagen:
    #         Imagen = Image.open(instance.Imagen.path)
    #         Imagen.save(instance.Imagen.path, quality=20, optimize = True)
        
    #     post_save.connect(optimize_image, sender = guia)

  
    

    
    




   
