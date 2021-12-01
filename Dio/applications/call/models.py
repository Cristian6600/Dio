from django.db import models
from applications.datos_g.models import Motivo
from applications.users.models import User
from simple_history.models import HistoricalRecords
from applications.guia.models import Guia
from applications.users.models import User
from applications.datos_g.models import datos_g
from django.conf import settings 

class Indicativo(models.Model):
    
    ind = models.IntegerField(
        verbose_name = 'Indicativo'
    )
    Region = models.CharField(
        max_length = 50
    )

    def __str__(self):
        return str(self.ind)

class Telefono(models.Model):
    cc = models.CharField(max_length =15)
    tel = models.CharField(primary_key=True, max_length=15)
    indicativo = models.ForeignKey(
        Indicativo, 
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.tel)

class Datos_t(models.Model):
    
    d_i = models.ForeignKey(datos_g,
        on_delete=models.CASCADE, verbose_name= "Seudo buscar"
        )

    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
        )
    # id_mot = models.ForeignKey(
    #     Motivo, 
    #     on_delete=models.CASCADE
    #     )

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
    entregas = models.ForeignKey(Guia, on_delete=models.CASCADE)
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE)
    pregunta_1= models.OneToOneField(Pregunta, on_delete=models.CASCADE, default = 1, blank = True, null = True)
    calificacion_1 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_1')
    pregunta_2= models.OneToOneField(Pregunta, on_delete=models.CASCADE, related_name="Pregunta_2", default= 2, blank = True, null = True)
    calificacion_2 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_2')
    pregunta_3= models.OneToOneField(Pregunta, on_delete=models.CASCADE, related_name="Pregunta_3", default = 3)
    calificacion_3 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_3')
    pregunta_4= models.OneToOneField(Pregunta, on_delete=models.CASCADE, related_name="Pregunta_4", default = 4)
    calificacion_4 = models.ForeignKey(calificacion, on_delete=models.CASCADE, related_name = 'calificacion_4')
    observacion = models.CharField(max_length = 30)
    fecha = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        blank=True, null=True, 
        editable=True,
        verbose_name= 'Usuario'
    )


    def __str__(self):
        return str(self.entregas)

    
