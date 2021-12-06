from django.urls import path, include
from rest_framework import routers
from .views import viewcarro,ViewCrudCarro

#importar UserViewSet da view
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'carros', CarroViewSet)
# router.register(r'car', viewcarro )

urlpatterns = [
    # path('', include(router.urls)),#registrando a rota de urls da api
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'car',viewcarro),
    path(r'crudcarro/<int:pk>/',ViewCrudCarro)
]