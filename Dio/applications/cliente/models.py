from django.db import models

class Ciudad (models.Model):
    id_ciu = models.CharField(
        max_length= 8, 
        primary_key = True,
        null=False,
        unique = True, 
    )
    Ciudad = models.CharField(
        max_length= 80
    )
    dep = models.CharField(
        max_length = 50
    )
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudad"

    def __str__(self):
        return str (self.Ciudad)

class Cliente (models.Model):
    id_clie = models.IntegerField(
        primary_key = True,
        verbose_name = 'Id cliente'
    )
    nit = models.CharField(
        max_length = 20
    )
    R_s = models.CharField(
        max_length = 70,
        verbose_name = 'Razon social'
    )
    Contact = models.CharField(
        max_length = 50,
        verbose_name = 'Contacto'
    )
    dir = models.CharField(
        max_length = 120,
        verbose_name = 'Direccion'
    )
    id_ciu = models.ForeignKey(
        Ciudad, 
        on_delete=models.CASCADE,
        verbose_name = 'Id ciudad'
    )
    tel = models.IntegerField(
        verbose_name = 'Tel fijo'
    )
    Cel = models.IntegerField(
        verbose_name = 'Celular'
    )
    ind = models.IntegerField(
        verbose_name = 'Indicativo'
    )
    Radicacion = models.IntegerField()

    Fact = models.CharField(
        max_length = 4,
        verbose_name = 'Factura'
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"

    def __str__(self):
        return self.nit

