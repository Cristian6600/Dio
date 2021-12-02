from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from applications.base_cliente.models import Bd_clie, Producto
from applications.cliente.models import Ciudad, Cliente
# from applications.fisico.models import Fisico
from applications.guia.models import Guia, Proceso

from django.dispatch import receiver
from django.db.models.signals import post_save

class Tipo(models.Model):
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

class Motivo(models.Model):
    
    id = models.IntegerField(primary_key=True, default = 0)

    motivo = models.CharField(
        max_length=50
    )

    id_tip = models.ForeignKey(
        Tipo, 
        on_delete=models.CASCADE,
        blank=True, 
        null=True
    )
    def __str__(self):
        return str(self.id) 
    
    class Meta:
        verbose_name = "Motivo"
        verbose_name_plural = "Motivo"

class datos_g (models.Model):
    id_datos_g = models.CharField(primary_key=True, max_length=30)

    seudo_dg = models.ForeignKey(
        Guia,
        on_delete=models.CASCADE,
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
    dest = models.CharField(
        max_length=100, blank=True, null = True
    )

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
    proceso = models.ForeignKey(Proceso,
        on_delete=models.CASCADE, blank = True, null = True
        )

    cod_vis = models.ForeignKey(
        'guia.Cod_vis',
        on_delete=models.CASCADE,
        blank = True,
        null = True,
    )

    gx = models.BigIntegerField(
        null=True,
        blank=True,
    )

    gy = models.BigIntegerField(
        null=True,
        blank=True,
    )

    mot = models.ForeignKey(
        Motivo, 
        on_delete=models.CASCADE, 
        verbose_name = 'motivo',
        null=True,
        blank=True,)

    id_estado = models.ForeignKey(
        'guia.Estado',
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Estado'
    )
    lote = models.IntegerField(
        blank=True, 
        null=True)

    cantidad = models.IntegerField(blank=True, null=True)

    orimp = models.IntegerField(
        blank=True,
        null=True,
        verbose_name = 'Orden impre '
        )

    zona = models.CharField(max_length=30, blank=True, null=True)
        
    class Meta:
        verbose_name = "Datos de gestion"
        verbose_name_plural = "Datos de gestion"
              
    def __str__(self):
        return str(self.seudo_dg)

    @property
    def desti(self):
        return self.dest

    @property
    def dire(self):
        return self.direccion

    @property
    def bar(self):
        return self.barrio

    @property
    def post(self):
        return self.postal

    @property
    def cod_vi(self):
        return self.cod_vis

    @property
    def motivo(self):
        return self.mot

    @property
    def id_est(self):
        return self.id_estado

    @property
    def ciudad(self):
        return (self.id_ciu)

    @property
    def documento(self):
        return (self.d_i)

    @property
    def or_imp(self):
        return self.orimp

    def save(self, *args, **kwargs):
        # self.seudo.bolsa  = self.vars
        self.seudo_dg.destinatario = self.desti
        self.seudo_dg.id_ciu = self.ciudad
        self.seudo_dg.direccion  = self.dire
        self.seudo_dg.barrio = self.bar
        self.seudo_dg.postal = self.post
        self.seudo_dg.cod_vis = self.cod_vi
        self.seudo_dg.mot = self.motivo
        self.seudo_dg.id_est = self.id_est
        self.seudo_dg.d_i = self.documento
        self.seudo_dg.or_imp = self.or_imp
        
        self.seudo_dg.save()

        super(datos_g, self).save(*args, **kwargs)

    
    




    