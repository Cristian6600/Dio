# from datetime import timedelta
# # django
# from django.db import models
# from django.utils import timezone
# from django.db.models import Q, F

# class ProductManager(models.Manager):
#     """ procedimiento modelo product """

#     def buscar_producto(self, kword, order):
#         consulta = self.filter(
#             Q(Guia__icontains=kword) | Q(Contiene=kword)
#         )