from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from PIL import Image
from model_utils.models import TimeStampedModel
from .managers import ProductManager
# from applications.call.models import Telefono
from applications.base_cliente.models import Bd_clie, Producto, Est_clie


from applications.users.models import User
from applications.cliente.models import Ciudad, Cliente

from applications.fisico.models import Fisico
# from applications.fisico.models import n_guia
from django.utils.encoding import smart_text
from django.conf import settings 

from simple_history.models import HistoricalRecords
from simple_history import register

class LogEntryManager(models.Manager):
        use_in_migrations = True

        def log_action(self, user_id, content_type_id, object_id, object_repr, action_flag, change_message=''):
            e = self.model(
            None, None, user_id, content_type_id, smart_text(object_id),
            object_repr[:200], action_flag, change_message
        )
            e.save()

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

class Guia(Fisico, TimeStampedModel):

    seudo = models.OneToOneField(
        Bd_clie,
        related_name = "guias",
        on_delete=models.CASCADE,
        primary_key=True)

    id_ser = models.ForeignKey(
        Servicio, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Servicio'       
    )    

    postal = models.CharField(
        max_length = 7,
        blank=True, 
        null=True,
    )

    id_clie = models.ForeignKey(
        Cliente,
        on_delete = models.CASCADE,
        blank=True, null=True)

        
    barrio = models.CharField(
        max_length = 70,
        null=True,
        blank=True,
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
    
    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )
    cantidad_vi = models.CharField(
        max_length= 10,
        verbose_name='Cantidad visitas',
        blank=True,
        null=True, 
        
        )
    
    codigo = models.CharField(
        max_length=28,
        blank=True, 
        null=True
        )

    or_imp = models.IntegerField(
        blank=True,
        null=True
        )

    tel = models.CharField(
        max_length=80,
        null=True, 
        blank = True
    )

    history = HistoricalRecords()    

    class Meta:
        verbose_name = "Guia"
        verbose_name_plural = "Guia"

        def __str__(self):
            return str(self.seudo) + self.destinatario

    objects = ProductManager()
    # objects = LogEntryManager()

    var_g = ("guia")

    # @property
    # def estado_cli(self):
    #     return self.codigo

    # Decorador concatenar ruta imagen
    @property
    def img(self):
      return self.var_g  + str(self.id_guia) + '.jpg'

    # """ def save(self, *args, **kwargs):
    #     self.imagen  = self.img
    #     super (Guia, self).save() """
      
    @property
    def userbd(self):
      return str(self.user)
        
    contador= 0  
    prueba = 0

    @property
    def can_vi(self):
        return str(self.cantidad_vi)

    @property
    def c_vis(self): 
        return str(self.cod_vis) 

    @property
    def moti(self):
        return str(self.mot.id)

    @property
    def motis(self):
        return str(self.mot.id)

    @property
    def estados(self):
        return self.id_est.id

    @property
    def cod(self):
        return (self.codigo)

    @property
    def concatenar(self):
        return  str(self.cantidad_vi) + (self.motis) + str(self.estados) + str(self.cod_vis) 

    def save(self, *args, **kwargs):
        
        self.imagen  = self.img
        # self.seudo.id_est_clie_id = self.codigo
        self.seudo.sucursal = self.userbd
        # self.seudo.id_est_clie = self.estado_cli
        self.codigo = self.concatenar   
        self.cantidad_vi = str(self.cod_vis) #codvis, captura el codigo de visita, para cantidad_vi
        # self.cantidad_vi = self.moti 
        if int(self.cantidad_vi) >=30:  #si cantidad_vi es mayor o igual a 30 retorneme a 0 "self.contador" 
            self.cantidad_vi = (self.contador)
            if self.suma >=3:   #quiere decir que al cumplir la condicion anterior es verdadera i si es mayor igual a 3 resetee el contador
                self.suma = self.contador

        elif int(self.cantidad_vi) <=29: #si la condicion anterior no era verdadera retorne cantidad y sum 
            self.cantidad_vi = self.suma

        self.cantidad_vi = int(self.moti) 
        print(self.cantidad_vi)
           #(self.fe[-14:-4])
        if self.cantidad_vi >= 16 and self.cantidad_vi >= 19:
            self.cantidad_vi = self.contador
            if self.suma >=3:
                self.suma = self.contador
        elif self.cantidad_vi >=16: #si la condicion anterior no era verdadera retorne cantidad y sum 
            self.cantidad_vi = self.suma
        else:self.cantidad_vi = self.contador
         
        self.seudo.save()       
        super(Guia, self).save(*args, **kwargs)

# [int(s) for s in str.split() if s.isdigit()]

    # candidate = form.save(commit=False)
    # candidate.user = request.user
    # candidate.save()

    # def optimize_image(sender, instance, **kwargs):.
    #     print("==========")
    #     print(instance)
    #     if instance.Imagen:
    #         Imagen = Image.open(instance.Imagen.path)
    #         Imagen.save(instance.Imagen.path, quality=20, optimize = True)
        
    #     post_save.connect(optimize_image, sender = guia)

# def optimize_image(sender, instance, **kwargs):
#     print("==========")
#     print(instance)
#     if instance.image:
#         image = Image.open(instance.image.path)
#         image.save(instance.image.path, quality=20, optimize = True)
        
# post_save.connect(optimize_image, sender = img)
    
    
class img(models.Model):
    
    id_guia = models.OneToOneField('fisico.Fisico', on_delete=models.CASCADE, blank = True, null = True)

    image = models.ImageField(
        upload_to = 'guia',
        null=True, 
        blank = True,   
    )
    fecha = models.DateTimeField(
        auto_now=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario',
        related_name='edited_by'
        
    )
    
    numero = models.CharField(max_length=30, blank=True, null=True)
    
    class Meta:
        verbose_name = "Imagenes Guia"
        verbose_name_plural = "Imagenes Guia"

    
    @property
    def fe(self):
        return str(self.image)

    # @receiver(post_save, sender=User)
    def save(self, *args, **kwargs, ):
        
        self.id_guia_id = (self.fe[-14:-4])
        self.id_guia.imagen =  str(self.fe)
        
        self.id_guia.save()     
        super (img, self).save(*args, **kwargs)
 

 
    

    
    

    
