from usuario.models import Carro, Usuario
from rest_framework import  serializers

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Usuario
#         fields = [
#             "url", "password", "last_login", "nome", "sobrenome", "genero", 
#             "cpf", "rg", "dataNascimento", "email", "cep", "bairro", "logradouro", 
#             "complemento", "numeroResidencia", "telefone", "numeroCelular", "idGroup", 
#             "dataHorarioCriacao", "dataDesativacao", "is_active", "is_staff", "is_superuser", 
#             "groups"
#         ]

class CalculatorCarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ["cor"]


class CarroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carro
        fields = ["nome","cor","ano"]