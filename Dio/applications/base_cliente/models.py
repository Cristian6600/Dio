from django.db import models
from django.conf import settings 
from applications.cliente.models import Cliente, Oficinas
from applications.argumento.models import Nom_producto, Proceso, Emision, Producto, Est_clie
from django.contrib.auth.models import User    
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .managers import BdManager

class Bd_clie (models.Model):

    seudo_bd = models.CharField(
        max_length=35,
        primary_key=True,       
    )

    id_clie = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        verbose_name = 'Id cliente'
    )
    
    t_emi = models.ForeignKey(
        Emision, 
        on_delete=models.CASCADE, 
        max_length = 4, 
        verbose_name = 'Tipo Emision'
    )

    archivo = models.CharField(
        max_length= 15,
        null=True,
        blank = True)

    MONTH_CHOICES = [
    ("AM", "AM"),
    ("PM", "PM"),
    ]
    jornada = models.CharField(
        max_length=3, 
        choices=MONTH_CHOICES, 
        null=True, 
        blank = True
    )
    
    canal = models.CharField(
        max_length=8, 
        null=True, 
        blank = True
    )
    realz = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True,
        verbose_name = 'Realzador'
    )
    tipo = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True
    )
    
    tarjeta = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True
    )
    id_est_clie = models.ForeignKey(
        Est_clie, 
        on_delete=models.CASCADE,
        verbose_name = 'Id estado cliente ',
        blank = True,
        null = True,

    )
    
    referencia = models.CharField(
        max_length= 50, 
        null=True, 
        blank = True
    )    
    convenio = models.CharField(
        max_length = 50, 
        null=True, 
        blank = True
    )
    id_serv = models.IntegerField(
        verbose_name = 'Id Servicio'
    )

    fecha = models.DateField()

    sucursal = models.CharField(
        max_length=50,
        blank=True,  null =True,
    )  

    nom_pro = models.ForeignKey(Nom_producto, on_delete=models.CASCADE, verbose_name='Nombre del producto')
    objects = BdManager()

    class Meta:
        verbose_name = "Base Cliente"
        verbose_name_plural = "Base Cliente"

    def __str__(self):
        return str(self.seudo_bd)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() 

