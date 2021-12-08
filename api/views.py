from rest_framework.response import Response
from .serializers import ResultadosSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
from .models import dados_rastreamento,resultados_michel
from math import radians, cos, sin, asin, sqrt

def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km

@api_view(['POST'])
def ViewCalcula_metricas(request):
    if request.method == 'POST':
        serializer = request.data
        
        DataInicio = datetime.strptime(serializer["datahora_inicio"], '%d/%m/%Y %H:%M:%S')
        DataFim = datetime.strptime(serializer["datahora_fim"], '%d/%m/%Y %H:%M:%S')
        Inicio = datetime.timestamp(DataInicio)
        Fim = datetime.timestamp(DataFim)
        
        listDadosRastreamentos = dados_rastreamento.objects.filter( serial=serializer["serial"],
                datahora__gte = Inicio,datahora__lte = Fim).order_by("datahora")


        tempo_em_movimento = 0
        tempo_parado = 0
        distancia_percorrida = 0
        
        if not listDadosRastreamentos:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

        for item in range(len(listDadosRastreamentos)):
            if listDadosRastreamentos[item].situacao_movimento:
                if not item == 0:
                    tempo_em_movimento += listDadosRastreamentos[item].datahora-listDadosRastreamentos[item-1].datahora
            else:
                if not item == 0:
                    tempo_parado += listDadosRastreamentos[item].datahora - listDadosRastreamentos[item-1].datahora
        
        print(timedelta(seconds=tempo_em_movimento))
        print(timedelta(seconds=tempo_parado))

        
        # for data in listDadosRastreamentos:
        #     
                 
        #         distancia_percorrida += haversine()


        
        objResultado = resultados_michel()
        objResultado.distancia_percorrida = distancia_percorrida
        objResultado.tempo_em_movimento = tempo_em_movimento
        objResultado.tempo_parado = tempo_parado
        objResultado.serial = serializer["serial"]
        # objResultado.save()

        return Response()


@api_view(['GET'])
def ViewRetorna_metricas(request):

 if request.method == 'GET':
        
        data = resultados_michel.objects.all()
        
        serializer = ResultadosSerializer(data,context={'request': request}, many=True)
        
        return Response(serializer.data)
            



