from django.db import models
from applications.base_cliente.models import bd_clie

class Fisico (models.Model):

    Bolsa = models.IntegerField()
    Seudo = models.ForeignKey(bd_clie, on_delete=models.CASCADE)
    Fecha = models.DateTimeField(auto_now=True)
    Estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Fisico"
        verbose_name_plural = "Fisico"
        unique_together = ('Bolsa', 'Seudo')

    def __str__(self):
        return str(self.Seudo)