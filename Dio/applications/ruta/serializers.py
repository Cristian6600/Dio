#
from rest_framework import serializers
#
from .models import Cargue, Fisico

class LenguajeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Fisico
    fields = ('__all__')



class ProgramadorSerializer(serializers.ModelSerializer):
  guia = LenguajeSerializer(many=False)
  class Meta:
    model = Cargue
    fields = ('mensajero', 'guia')