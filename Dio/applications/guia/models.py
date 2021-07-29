from django.db import models
from applications.fisico.models import Fisico
from applications.cliente.models import Cliente
from applications.base_cliente.models import bd_clie, Producto
from applications.users.models import User
from django.db.models.signals import post_save
from PIL import Image
# from .managers import ProductManager


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
        return str(self.id_serv)
    
class guia (models.Model):

    id = models.IntegerField(
        primary_key = True, 
        unique=True,
        verbose_name = 'Guia'
    )
    Bolsa = models.ForeignKey(
        Fisico, 
        on_delete=models.CASCADE 
    )
    id_serv = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE
    )
    id_clie = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE
    )
    d_i = models.ForeignKey(
        bd_clie, 
        on_delete=models.CASCADE 
    ) 

    m = models.IntegerField(
        default=1
    )
    Ancho = models.IntegerField(
        default=1
    )
    Alto = models.IntegerField(
        default=1
    )
    Largo = models.IntegerField(
        default=1
    )
    Copia = models.IntegerField(
        default=1
    )
    Unidad = models.IntegerField(
        default=1
    )
    Contiene = models.CharField(
        max_length = 50
    )
    Orden = models.IntegerField()

    Domicilio = models.IntegerField(
        default=0
    )
    Acarreo = models.IntegerField(
        default=0
    )
    Flete = models.IntegerField(
        default=0
    )
    Declarado = models.IntegerField(
        default=0
    )
    Fecha = models.DateTimeField()
    
    id_mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE, 
        verbose_name= 'id Motivo'
    )

    Imagen = models.ImageField(
        upload_to = 'guia',
        blank= True
    )

    id_est = models.ForeignKey(
        Estado,
         on_delete=models.CASCADE
    )

    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE
    )

    # objects = ProductManager()
    class Meta:
        verbose_name = "guia"
        verbose_name_plural = "guia"
        
    def __str__(self):
        return str(self.id)
    
def optimize_image(sender, instance, **kwargs):
    print("==========")
    print(instance)
    if instance.Imagen:
        Imagen = Image.open(instance.Imagen.path)
        Imagen.save(instance.Imagen.path, quality=20, optimize = True)

post_save.connect(optimize_image, sender = guia)

   
