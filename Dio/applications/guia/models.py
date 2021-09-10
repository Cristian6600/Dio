from django.db import models
from applications.cliente.models import Cliente
from applications.datos_g.models import datos_g
from django.conf import settings 
from applications.base_cliente.models import bd_clie, Producto
from applications.courrier.models import courrier
from django.contrib.auth.models import User 




from django.utils.encoding import smart_text

from django.db.models.signals import post_save
from PIL import Image
# from .managers import ProductManager
# from simple_history.models import HistoricalRecords
# from simple_history import register

class LogEntryManager(models.Manager):
        use_in_migrations = True

        def log_action(self, user_id, content_type_id, object_id, object_repr, action_flag, change_message=''):
            e = self.model(
            None, None, user_id, content_type_id, smart_text(object_id),
            object_repr[:200], action_flag, change_message
        )
            e.save()

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
    
class guia(datos_g):

    gui = models.BigAutoField(
        primary_key=True,     

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
        
    m = models.IntegerField(
        default=1, 
        null=True, 
        blank = True
    )
    ancho = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    alto = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    largo = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    copia = models.IntegerField(
        default=1,
        null=True, 
        blank = True
    )
    unidad = models.IntegerField(
        default=1, 
        null=True, 
        blank = True
    )
    contiene = models.CharField(
        max_length = 50, 
        null=True, 
        blank = True
    )
    orden = models.IntegerField(
        null=True, 
        blank = True
    )

    domicilio = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    acarreo = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    flete = models.IntegerField(
        default=0,
        null=True, 
        blank = True
    )
    declarado = models.IntegerField(
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

    cantidad = models.PositiveIntegerField(
        default=0 ,
        verbose_name = 'Cantidad recepcion '
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario')
    
    objects = LogEntryManager()

    
    # history = HistoricalRecords()    

    # objects = ProductManager()
    
    # Decorador para imagen
    @property
    def varg(self):
      return 'gui/' + str(self.id) + '.jpg'

    def save(self, *args, **kwargs):
        self.Imagen  = self.varg
        super (guia, self).save()
     
    class Meta:
        verbose_name = "Guia"
        verbose_name_plural = "Guia"
   
    def __str__(self):
        return str(self.gui) + ' ' + str(self.id_est)
    
    #Decorador Guardado
    @property
    def bolsas(self):
      return str(self.bolsa)

    def save(self, *args, **kwargs,):
        self.id.bolsa  = self.bolsa
        self.id.save()
        super(guia, self).save(*args, **kwargs)

    

    # candidate = form.save(commit=False)
    # candidate.user = request.user
    # candidate.save()


    # def optimize_image(sender, instance, **kwargs):
    #     print("==========")
    #     print(instance)
    #     if instance.Imagen:
    #         Imagen = Image.open(instance.Imagen.path)
    #         Imagen.save(instance.Imagen.path, quality=20, optimize = True)
        
    #     post_save.connect(optimize_image, sender = guia)




    




   
