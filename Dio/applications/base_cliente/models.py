from django.db import models

from applications.cliente.models import Cliente

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
        max_length = 50
    )
    Tipo = models.CharField(
        max_length = 5,
        verbose_name = 'Tipos distribucion'
    )
    Homologacion = models.CharField(
        max_length=50
    )

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Producto"
        unique_together = ('id_pro', 'id_clie')

    def __str__(self):
        return self.producto

class est_clie (models.Model):

    id_est_clie = models.IntegerField(
        primary_key = True
    )
    Estado = models.CharField(max_length = 35)
    Descripcion = models.CharField(max_length = 35)
    Proceso = models.CharField(max_length = 20)
    

    verbose_name = "Estado Cliente"
    verbose_name_plural = "Estado del cliente"

    def __str__(self):
        return str (self.id_est_clie)

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

class bd_clie (models.Model):

    Seudo = models.CharField(
        max_length=35,
        primary_key=True
    )

    id_clie = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        verbose_name = 'Id cliente'
    )
    Archivo = models.CharField(
        max_length= 15,
        null=True,
        blank = True)

    MONTH_CHOICES = [
    ("AM", "AM"),
    ("PM", "PM"),
    ]
    Jornada = models.CharField(
        max_length=3, 
        choices=MONTH_CHOICES, 
        null=True, 
        blank = True
    )
    Id_pro = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE,
        verbose_name = 'Id producto'
    )
    D_i = models.IntegerField(
        null=True, 
        blank = True, 
        verbose_name = 'Documento de identidad'
    )
    Cliente = models.CharField(
        max_length = 150, 
        null=True, 
        blank = True
    )
    
    Id_Proc = models.IntegerField(
        null=True, 
        blank = True
    )
    ofi = models.CharField(
        max_length=8, 
        null=True, 
        blank = True,
        verbose_name= 'Oficina'
    )
    Canal = models.CharField(
        max_length=8, 
        null=True, 
        blank = True
    )
    Realz = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True,
        verbose_name = 'Realzador'
    )
    Tipo = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True
    )
    D_i_a = models.IntegerField(
        null=True, 
        blank = True,
        verbose_name = 'Documento identidad autorizado'
    )
    Autor = models.CharField(
        max_length=100, 
        null=True, 
        blank = True, 
        verbose_name = 'Autorizado'
    )
    Tarjeta = models.CharField(
        max_length = 30, 
        null=True, 
        blank = True
    )
    Codigo = models.IntegerField(
        null=True, 
        blank = True
    )
    id_est_clie = models.ForeignKey(
        est_clie, 
        on_delete=models.CASCADE,
        verbose_name = 'Id estado cliente '
    )
    orden = models.IntegerField(
        null = True, 
        blank = True
    )
    Referencia = models.CharField(
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
    Bolsa = models.IntegerField(
        null = True, 
        blank = True
    )
    fecha = models.DateTimeField(
        auto_now=True
    )
    T_emi = models.ForeignKey(
        Emision, 
        on_delete=models.CASCADE, 
        max_length = 4, 
        verbose_name = 'Tipo Emision'
    )
    
    class Meta:
        verbose_name = "Base Cliente"
        verbose_name_plural = "Base Cliente"

    def __str__(self):
        return str(self.Seudo)