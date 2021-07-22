from django.db import models
from applications.base_cliente.models import bd_clie

class Fisico (models.Model):

    Bolsa = models.IntegerField()
    Seudo = models.CharField(max_length=35)
    Fecha = models.DateTimeField(auto_now=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Fisico"
        verbose_name_plural = "Fisico"
        unique_together = ('Bolsa', 'Seudo')

    def __str__(self):
        return str(self.Seudo)