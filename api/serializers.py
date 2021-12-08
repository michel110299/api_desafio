from rest_framework import  serializers
from .models import resultados_michel

class ResultadosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = resultados_michel
        fields = ["distancia_percorrida","tempo_em_movimento","tempo_parado","serial","centroides_paradas"]


