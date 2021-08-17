from django.db import models

from applications.cliente.models import Ciudad

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

#class dependencia(models.Model):
 #   Dependencia = models.CharField(max_length=25)

  #  def __str__(self):
   #     return self.Dependencia

class Areas(models.Model):
    Areas = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.Areas

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )
    username = models.CharField(
        max_length=20, 
        unique=True,
        verbose_name= 'Usuario'
    )
    email = models.EmailField()

    nombres = models.CharField(
        max_length=30, 
        blank=True
    )
    apellidos = models.CharField(
        max_length=30, 
        blank=True
    )
    genero = models.CharField(
        max_length=1, 
        choices=GENDER_CHOICES, 
        blank=True
    )
    
    ciudad = models.OneToOneField(
        Ciudad,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    is_staff = models.BooleanField(
        default=True
    )
    is_active = models.BooleanField(
        default=False
    )

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email',]   

    objects = UserManager()

    class Meta:
        verbose_name = "Permisos de usuarios"
        verbose_name_plural = "Permisos de usuario"

    def __str__(self):
        return str(self.ciudad) + ' ' +self.nombres

    def get_short_name(self):
         return str(self.nombres + ' ' + self.apellidos )
    
    # def get_full_name (self):
    #     return str(self.nombres + ' ' + self.apellidos + '')