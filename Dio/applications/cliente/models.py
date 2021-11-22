from django.db import models


class Departamento(models.Model):
    departamento = models.CharField(max_length=30)

    def __str__(self):
        return self.departamento

class Ciudad (models.Model):
    id = models.CharField(
        max_length=10,
        primary_key = True,
        unique = True, 
        verbose_name = 'Dane'
    )
    ciudad = models.CharField(
        max_length= 80
    )
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE,
        verbose_name = 'Departamento'
    )

    cubrimiento = models.CharField(
        max_length=15,
        null = True,
        blank = True
    )

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudad"

    def __str__(self):
        return str (self.ciudad) 

class Cliente (models.Model):
    id_clie = models.IntegerField(
        primary_key = True,
        verbose_name = 'Id cliente'
    )
    nit = models.CharField(
        max_length = 20
    )
    r_s = models.CharField(
        max_length = 70,
        verbose_name = 'Razon social'
    )
    contact = models.CharField(
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
    cel = models.IntegerField(
        verbose_name = 'Celular'
    )
    ind = models.IntegerField(
        verbose_name = 'Indicativo'
    )
    radicacion = models.IntegerField()

    fact = models.CharField(
        max_length = 4,
        verbose_name = 'Factura'
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Cliente"

    def __str__(self):
        return self.nit






    