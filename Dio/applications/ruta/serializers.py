from rest_framework import serializers

from .models import Cargue
from applications.fisico.models import Fisico




class CargueSerializer(serializers.ModelSerializer):
    guia = serializers.PrimaryKeyRelatedField(queryset=Fisico.objects.all(), many=True)
    class Meta:
        model = Cargue
        fields = ('guia', 'full_name', )
        
class FisicoSerializer(serializers.ModelSerializer):
    guia = CargueSerializer(many=True, read_only=True)
    
    class Meta:
        model = Fisico
        fields = ('__all__')
        

    