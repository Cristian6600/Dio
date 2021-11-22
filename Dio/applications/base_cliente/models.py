from django.db import models
from django.conf import settings 
from applications.cliente.models import Cliente
from django.contrib.auth.models import User    
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Producto (models.Model):
    id_pro = models.CharField(  
        primary_key = True,     
        unique = True,
        max_length = 5,
        verbose_name = 'Id producto'
    )
    id_clie = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        verbose_name = 'Id cliente'
    )
    producto = models.CharField(
        max_length = 50
    )
    Proceso = models.CharField(
        max_length = 50, blank = True, null = True,
    )
    tipo = models.CharField(
        max_length = 5,
        verbose_name = 'Tipos distribucion', blank = True, null = True,
    )
    homologacion = models.CharField(
        max_length=50, blank = True, null = True,
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"
        unique_together = ('id_pro', 'id_clie')

    def __str__(self):
        return str(self.id_pro)+ '-' + self.producto

class Est_clie (models.Model):

    id = models.CharField(
        primary_key = True,
        max_length = 10
    )
    cod_est = models.IntegerField()
    estado = models.CharField(max_length = 55)
    descripcion = models.CharField(max_length = 55)
    proceso = models.CharField(max_length = 20)
    
    verbose_name = "Estado Cliente"
    verbose_name_plural = "Estado del cliente"

    def __str__(self):
        return str (self.id)

class Emision(models.Model):
    t_emi = models.CharField(
        primary_key = True, 
        max_length=4, 
        verbose_name = 'Tipo emision'
    )

    emision = models.CharField(
        max_length= 35
    )
    
    class Meta:
        verbose_name = "Emision"
        verbose_name_plural = "Emision"

    def __str__(self):
        return self.emision

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
    id_pro = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        verbose_name = 'Id producto'
    )
    d_i = models.CharField(
        max_length = 13,
        null=True, 
        blank = True, 
        verbose_name = 'Documento de identidad'
    )
    cliente = models.CharField(
        max_length = 150, 
        null=True, 
        blank = True
    )
    
    id_proc = models.IntegerField(
        null=True, 
        blank = True
    )
    ofi = models.CharField(
        max_length=8, 
        null=True, 
        blank = True,
        verbose_name= 'Oficina'
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
    d_i_a = models.IntegerField(
        null=True, 
        blank = True,
        verbose_name = 'CC autorizado'
    )
    autor = models.CharField(
        max_length=100, 
        null=True, 
        blank = True, 
        verbose_name = 'Autorizado'
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
    orden = models.IntegerField(
        null = True, 
        blank = True
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
    bolsa = models.IntegerField(
        null = True, 
        blank = True
    )
    guia = models.IntegerField(
        blank = True, 
        null = True, 
    )

    fecha = models.DateTimeField(
        auto_now=True
    )

    fe_fisico = models.DateTimeField(
        auto_now=None,
        blank=True,
        null=True,
        verbose_name = 'Fecha fisico')

    sucursal = models.CharField(
        max_length=50,
        blank=True,  null =True,
    )   
    
        
    class Meta:
        verbose_name = "Base Cliente"
        verbose_name_plural = "Base Cliente"

    def __str__(self):
        return str(self.seudo_bd)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() 

