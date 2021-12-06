from usuario.models import Carro
from rest_framework.response import Response
from .serializers import CarroSerializer,CalculatorCarroSerializer
from rest_framework.decorators import api_view
from rest_framework import status

# #importar UserSerializer do forms
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = Usuario.objects.all()
#     serializer_class = UserSerializer

# #importar UserSerializer do forms
# class CarroViewSet(viewsets.ModelViewSet):
#     queryset = Carro.objects.all()
#     serializer_class = CarroSerializer


@api_view(['GET', 'POST'])
def viewcarro(request):
    if request.method == 'GET':
        data = Carro.objects.all()
        serializer = CalculatorCarroSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    
    elif request.method == 'POST':
        serializer = CalculatorCarroSerializer(data=request.data)
        
        if serializer.is_valid():
            # serializer.save()
            
            listCarro = Carro.objects.filter(cor__contains=serializer.data["cor"])
            print(listCarro)
            for carro in listCarro:
                carro.nome="cassetinho"
                carro.save()
            
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ViewCrudCarro(request, pk):
    try:
        objCarro = Carro.objects.get(pk=pk)
    except Carro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarroSerializer(objCarro)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CarroSerializer(objCarro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        objCarro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)