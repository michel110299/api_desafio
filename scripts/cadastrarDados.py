import json
from api.models import dados_rastreamento
import json
"""
python manage.py shell
exec(open('scripts/cadastrarDados.py').read())
"""

with open("scripts/dados.json") as jsonFile:
    listdados_rastreamento = json.load(jsonFile)
    jsonFile.close()
list_obj_listdados_rastreamento = []

for dado in listdados_rastreamento:
    obj_cidade = dados_rastreamento(serial = dado['serial'], ignicao = json.loads(dado['ignicao'].lower()) ,velocidade = float(dado['velocidade']) ,situacao_movimento = json.loads(dado['situacao_movimento'].lower()), latitude = float(dado['latitude']), 
        longitude = float(dado['longitude']), orientacao = float(dado['orientacao']), datahora = int(dado['datahora']))
    list_obj_listdados_rastreamento.append(obj_cidade)
dados_rastreamento.objects.bulk_create(list_obj_listdados_rastreamento)