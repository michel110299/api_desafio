from rest_framework.response import Response
from .serializers import ResultadosSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime
from .models import dados_rastreamento,resultados_michel
from sklearn.cluster import KMeans
from .validade import qick_distance


@api_view(['POST'])
def ViewCalcula_metricas(request):
    if request.method == 'POST':
        serializer = request.data
        
        DataInicio = datetime.strptime(serializer["datahora_inicio"], '%d/%m/%Y %H:%M:%S')
        DataFim = datetime.strptime(serializer["datahora_fim"], '%d/%m/%Y %H:%M:%S')
        Inicio = datetime.timestamp(DataInicio)
        Fim = datetime.timestamp(DataFim)
        
        listDadosRastreamentos = dados_rastreamento.objects.filter(serial=serializer["serial"],
            datahora__gte = Inicio,datahora__lte = Fim).order_by("datahora")

        tempo_em_movimento = 0
        tempo_parado = 0
        distancia_percorrida = 0
        quantidadeParadas = 0
        
        if not listDadosRastreamentos:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        for item in range(len(listDadosRastreamentos)):
            if not item == 0:
                if listDadosRastreamentos[item].situacao_movimento == True:
                    tempo_em_movimento += listDadosRastreamentos[item].datahora-listDadosRastreamentos[item-1].datahora
                else:
                    tempo_parado += listDadosRastreamentos[item].datahora - listDadosRastreamentos[item-1].datahora
            
            if not item == len(listDadosRastreamentos)-1:
                distancia_percorrida += qick_distance(listDadosRastreamentos[item].latitude,listDadosRastreamentos[item].longitude,listDadosRastreamentos[item+1].latitude,listDadosRastreamentos[item+1].longitude)

                if listDadosRastreamentos[item].situacao_movimento and not listDadosRastreamentos[item].situacao_movimento:
                    quantidadeParadas+=1
        
        distancia_percorrida=round(distancia_percorrida, 1)
        
        response = {
            "distancia_percorrida": distancia_percorrida,
            "tempo_em_movimento": tempo_em_movimento, 
            "tempo_parado": tempo_parado,
            "centroides_paradas":None,
            "serial": serializer["serial"]
        }
        
        
        objResultado = resultados_michel()
        objResultado.distancia_percorrida = distancia_percorrida
        objResultado.tempo_em_movimento = tempo_em_movimento
        objResultado.tempo_parado = tempo_parado
        objResultado.serial = serializer["serial"]
        objResultado.save()

        return Response(response)


@api_view(['GET'])
def ViewRetorna_metricas(request):

 if request.method == 'GET':
        
        data = resultados_michel.objects.all()
        
        serializer = ResultadosSerializer(data,context={'request': request}, many=True)
        
        return Response(serializer.data)
            



