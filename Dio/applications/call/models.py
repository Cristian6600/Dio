from django.db import models

from applications.users.models import User
from simple_history.models import HistoricalRecords
from applications.guia.models import Guia
from applications.users.models import User
from applications.datos_g.models import datos_g
from applications.argumento.models import Motivo_call
from django.conf import settings 


class Tel(models.Model):
    telefono= models.CharField(primary_key=True, max_length=12)

    def __str__(self):
        return self.telefono

class Indicativo(models.Model):
    
    ind = models.CharField(
        max_length = 10,
        verbose_name = 'Indicativo'
    )
    Region = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return str(self.ind)

class Telefono(models.Model):
    id = models.OneToOneField(Guia,on_delete=models.CASCADE, primary_key=True, max_length=12)
    tel = models.CharField(max_length=80)
    indicativo = models.ForeignKey(
        Indicativo, 
        on_delete=models.CASCADE,
    )
    fecha_call = models.DateTimeField(
        auto_now_add=True
    )
    motivo_call = models.ForeignKey(
        Motivo_call, 
        on_delete=models.CASCADE,
        blank=True,
        null=True)
    observacion = models.TextField(max_length=200)
    
    def __str__(self):
        return str(self.tel)

    @property
    def telefono(self):
        return str(self.tel)

    def save(self, *args, **kwargs, ):
        
        self.id.tel = self.telefono
        
        self.id.save()     
        super (Telefono, self).save(*args, **kwargs)

class Datos_t(models.Model):
    
    d_i = models.CharField(max_length=12,
        verbose_name= "Seudo buscar"
        )

    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
        )

    activo = models.BooleanField(
        default=True
    )
    history = HistoricalRecords()

    class Meta:
        verbose_name = "Gestion"
        verbose_name_plural = "Gestion"
    
    def __str__(self):
        return str(self.telefono)

class calificacion(models.Model):
    calficacion = models.CharField(max_length=22)

    def __str__ (self):
        return str(self.calficacion)

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=80)

    def __str__(self):
        return self.pregunta

class Auditoria(models.Model):
    calificacionn_5 = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    entregas = models.ForeignKey(Guia, on_delete=models.CASCADE)
    pregunta_1= models.CharField(max_length=70, default = 'CUENTA USTED YA CON LA TC', blank = True, null = True)
    calificacion_1 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_1', blank = True, null = True)
    pregunta_2= models.CharField(max_length=70, default = 'BOLSA DEBIDAMENTE SELLADA', blank = True, null = True)
    calificacion_2 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_2', blank = True, null = True)
    pregunta_3= models.CharField(max_length=70, default = 'SOLICITO SU DOCUMENTO DE IDENTIDAD', blank = True, null = True)
    calificacion_3 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_3', blank = True, null = True)
    pregunta_4= models.CharField(max_length=70, default = 'FIRMO USTED EL ACUSE DE RECIBIDO', blank = True, null = True)
    calificacion_4 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_4', blank = True, null = True)
    
    pregunta_5= models.CharField(max_length=70, default = 'CALIFIQUE DE 1 A 5 EL SERVICIO', blank = True, null = True)
    
    calificacion_5 = models.CharField(
        max_length=2,
        choices=calificacionn_5,
        blank = True, null = True
    )
    observacion = models.CharField(
        max_length = 30,
        blank = True, null = True
        )
    fecha = models.DateTimeField(auto_now=True, blank= True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )

    motivo_call = models.ForeignKey(Motivo_call, on_delete=models.CASCADE) 

    def __str__(self):
        return str(self.entregas)

    @property
    def motivo(self):
        return int(self.motivo_call.id)    

    def save(self, *args, **kwargs):
        
        if  2 <= self.motivo <= 3: 
            self.entregas.estado = self.entregas.estado = 1
            
        else:
            self.entregas.estado = 0

        self.entregas.save()       
        super(Auditoria, self).save(*args, **kwargs)

