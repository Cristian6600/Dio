from django.db import models
from django.conf import settings 
from applications.base_cliente.models import Bd_clie
from applications.cliente.models import Ciudad
from applications.courrier.models import courrier
from applications.argumento.models import Estado, Motivo, Cod_vis, Proceso, Est_clie
from simple_history.models import HistoricalRecords

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
        Motivo, 
        on_delete=models.CASCADE, 
        verbose_name = 'motivo',
        null=True,
        blank=True,
        default = 0)  

    id_est = models.ForeignKey(
        Estado, 
        on_delete=models.CASCADE, 
        null=True, 
        blank = True,
        verbose_name = 'Estado',
        default= 2
    )

    fecha_bolsa = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.bolsa)

class Fisico(Fisi_pa, Bolsa):

    id_guia = models.AutoField(primary_key=True)

    direccion = models.CharField(max_length=240, blank = True, null=True)

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

    cod_vis = models.ForeignKey(
        Cod_vis,
        on_delete=models.CASCADE,
        blank = True,
        null = True,
        default= 0
    )
   
    proceso = models.ForeignKey(Proceso,
        on_delete=models.CASCADE, 
        blank=True, null=True
        )
    destinatario = models.CharField(max_length=100, blank=True, null=True)

    d_i = models.CharField(max_length=15, blank = True, null=True)

    fecha_recepcion = models.DateTimeField(auto_now=True, blank = True, null= True, verbose_name='Fecha gestion')

    fecha_planilla = models.DateTimeField(auto_now=True, blank= True, null= True)

    mensajero = models.ForeignKey(
        courrier, 
        on_delete=models.CASCADE, 
        blank = True, null= True
        )
    
    est_planilla = models.CharField(max_length= 30 )

    id_planilla = models.IntegerField(blank=True, null= True)

    cantidad_vi = models.IntegerField(
        default = 0,
        verbose_name='Cantidad visitas', #lleva valor definitivo contador
        blank=True,
        null=True, 
        
        )

    codigo = models.CharField(
        max_length=28,
        blank=True, 
        null=True
        )
    
    cod_ins = models.ForeignKey(
        Est_clie,
        on_delete=models.CASCADE, 
        blank = True, null= True
    )
    users = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        verbose_name= 'Usuario Descargue'
    )
    fecha_descargue = models.DateField(
        blank=True,
        null=True,
        verbose_name= 'Descargue'
    )
    origen = models.CharField(
        max_length=60, 
        blank=True, null=True)

    destino = models.CharField(
        max_length=60, 
        blank=True, null=True)

    history = HistoricalRecords()    
    
    unique_together = ('bolsa', 'seudo')

    def __str__(self):
        return str(self.id_guia)

     #### concatenar codigo
    @property
    def can_vi(self):
        return str(self.cantidad_vi) 

    @property
    def motis(self):
        return str(self.mot.id) 

    @property
    def estados(self):
        return self.id_est.id 

    @property
    def c_vis(self): 
        return str(self.cod_vis) 

    ############################################  
    #  contador para generar reset
    contador= 0  

    @property
    def concatenar(self):
        return  str(self.cantidad_vi) + (self.motis) + str(self.estados) + str(self.cod_vis) 

    @property
    def cant_vi(self):
        return str(self.cantidad_vi)

    @property
    def prueba(self):
        return str(self.codigo)



    def save(self, *args, **kwargs):
        self.codigo = self.concatenar 
        self.cod_ins_id = self.prueba

        super(Fisico, self).save(*args, **kwargs)

class Paquete(Fisi_pa):
    
    bolsa = models.ForeignKey(
        Bolsa, 
        on_delete=models.CASCADE, 
        related_name = 'bolsa_p')

    seudo = models.OneToOneField(
        Bd_clie,
        primary_key = True,
        on_delete=models.CASCADE,
        unique = True,
        related_name = 'bd_paquete'
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
        self.seudo.fisico  = self.seudo.fisico = 1
        
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

class Cobertura(models.Model):
    bolsa = models.OneToOneField(Bolsa, on_delete=models.CASCADE, primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )
    fecha = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name= 'Fecha fisico'
    )
    estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE
    )

    @property
    def estados(self):
        return str(self.estado.id)

    def __str__(self):
        return str(self.bolsa)

    def save(self, *args, **kwargs):
        self.bolsa.id_est_id  = self.estados
        
        self.bolsa.save()

        super(Cobertura, self).save(*args, **kwargs)


