from tabnanny import verbose
from django.db import models
# from applications.base_cliente.models import Bd_clie
# from applications.guia.models import Servicio, Cod_vis, Estado
from django.conf import settings 

from applications.base_cliente.models import Bd_clie, Producto, Est_clie
from applications.cliente.models import Ciudad
from applications.courrier.models import courrier

from django.dispatch import receiver
from django.db.models.signals import post_save
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError


class Proceso(models.Model):
    
    id = models.IntegerField(primary_key=True)
    proceso = models.CharField(
        max_length=30
        )
    cod_dir = models.CharField(max_length=4)

    def __str__(self):
        return str(self.id)

class Fisi_pa(models.Model):

    fecha = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name= 'Fecha fisico'
    )
    estado = models.BooleanField(
        default=True
    )
    class Meta:
        abstract = True

class Bolsa(models.Model):
    bolsa = models.IntegerField(primary_key=True)

    mot = models.ForeignKey(
        'datos_g.Motivo', 
        on_delete=models.CASCADE, 
        verbose_name = 'motivo',
        null=True,
        blank=True,
        default = 4)  

    def __str__(self):
        return str(self.bolsa)

class Fisico(Fisi_pa, Bolsa):

    id_guia = models.AutoField(primary_key=True)

    direccion = models.CharField(max_length=100, blank = True, null=True)

    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'ciudad',
        null=True,
        blank=True,
    )
    cantidad = models.PositiveIntegerField(
        default=0,
        verbose_name = 'Cantidad Total',
        blank = True,
        null = True, 
    )

    suma = models.IntegerField(
        blank = True,
        null = True,
        default= 0
    )

    cod_vis = models.ForeignKey(
        'guia.Cod_vis',
        on_delete=models.CASCADE,
        blank = True,
        null = True,
        default= 0
    )

    id_est = models.ForeignKey(
        'guia.Estado', 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Estado',
        default= 4
    )
    proceso = models.ForeignKey('Proceso',
        on_delete=models.CASCADE, 
        blank=True, null=True
        )
    destinatario = models.CharField(max_length=100, blank=True, null=True)

    d_i = models.CharField(max_length=15, blank = True, null=True)

    fecha_recepcion = models.DateTimeField(blank = True, null= True, verbose_name='Fecha gestion')

    fecha_planilla = models.DateTimeField(auto_now=True, blank= True, null= True)

    imagen = models.ImageField(
        upload_to = 'guia',
        null=True, 
        blank = True,   
    )
    mensajero = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, 
        blank = True, null= True
        )
    
    est_planilla = models.CharField(max_length= 30 )

    id_planilla = models.IntegerField(blank=True, null= True)

    history = HistoricalRecords()    
    
    unique_together = ('bolsa', 'seudo')

    def __str__(self):
        return str(self.id_guia)

    @property
    def cant_vi(self):
        return str(self.cantidad_vi)

    

class Paquete(Fisi_pa):
    
    bolsa = models.IntegerField()

    seudo = models.OneToOneField(
        Bd_clie,
        primary_key = True,
        on_delete=models.CASCADE,
        unique = True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )
    class Meta:
        unique_together = ('bolsa', 'seudo')

    @property
    def var(self):
      return (self.bolsa)

    def save(self, *args, **kwargs):
        self.seudo.bolsa  = self.var
        
        self.seudo.save()

        super(Paquete, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.seudo) 
    
class Motivo_mesa(models.Model):
    motivo = models.CharField(max_length=100)

    def __str__(self):
        return str(self.motivo)

class Mesa(models.Model):
    guia = models.ForeignKey(Fisico, on_delete=models.CASCADE)
    id_motivo_m = models.ForeignKey(Motivo_mesa, on_delete=models.CASCADE, verbose_name= 'motivo')
    observacion = models.CharField(max_length=200)
    
    class Meta:
        verbose_name = 'inconsistencias'
        verbose_name_plural = 'inconsistencias'

    def __str__(self):
        return str(self.guia)






