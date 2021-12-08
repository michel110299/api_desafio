from django.db import models

class dados_rastreamento(models.Model):
    serial = models.CharField(verbose_name = 'Serial', max_length = 194)
    ignicao = models.BooleanField(verbose_name = 'ignicao')
    situacao_movimento = models.BooleanField(verbose_name = 'situacao movimento' )
    velocidade = models.FloatField(verbose_name = 'velocidade' )
    latitude = models.FloatField(verbose_name = 'latitude' )
    longitude = models.FloatField(verbose_name = 'longitude' )
    orientacao = models.FloatField(verbose_name = 'orientação' )
    datahora = models.IntegerField(verbose_name = 'data hora' )

    class Meta:
        verbose_name = "dado do rastreamento"
        verbose_name_plural = "dados do rastreamento"

    def __str__(self):
        return self.serial

class coordenada(models.Model):
    latitude = models.FloatField(verbose_name = 'latitude' )
    longitude = models.FloatField(verbose_name = 'longitude' )

    class Meta:
        verbose_name = "Coordenada"
        verbose_name_plural = "Coordenadas"


    def __str__(self):
        return f"{self.latitude} {self.longitude}"


class resultados_michel(models.Model):
    distancia_percorrida = models.FloatField(verbose_name = 'distancia percorrida' )
    tempo_em_movimento = models.IntegerField(verbose_name = 'Tempo em movimento' )
    tempo_parado = models.IntegerField(verbose_name = 'tempo parado')
    centroides_paradas = models.ManyToManyField(coordenada,related_name="centroides_paradas_resultados_michel")
    serial = models.CharField(verbose_name = 'Nome', max_length = 194)


    class Meta:
        verbose_name = "Resultado Michel"
        verbose_name_plural = "Resultados Michel"

    def __str__(self):
        return self.serial