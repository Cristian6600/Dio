#
from rest_framework import serializers
#
from .models import Lenguaje, Programador

class LenguajeSerializer(serializers.ModelSerializer):

  class Meta:
    model = Lenguaje
    fields = ('__all__')



class ProgramadorSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Programador
    fields = ('__all__')