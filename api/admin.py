from django.contrib import admin
from .models import dados_rastreamento,resultados_michel,coordenada

admin.site.register(resultados_michel)
admin.site.register(dados_rastreamento)
admin.site.register(coordenada)