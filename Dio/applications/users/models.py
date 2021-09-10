from django.db import models
from django.core.signals import request_finished
from django.conf import settings
from django.dispatch import receiver

from applications.cliente.models import Ciudad

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager

from django.db.models.signals import post_save

from django.dispatch import receiver




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

    def get_short_name(self):
         return str(self.nombres + ' ' + self.apellidos )

    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()   

