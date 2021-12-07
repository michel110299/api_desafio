from django.urls import path, include
from .views import ViewCalcula_metricas,ViewRetorna_metricas



urlpatterns = [
    # path('', include(router.urls)),#registrando a rota de urls da api
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'calcula_metricas',ViewCalcula_metricas),
    path(r'retorna_metricas',ViewRetorna_metricas)
    
]