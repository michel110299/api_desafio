from django.db import models

class dados_rastreamento(models.Model):
    serial = models.CharField(verbose_name = 'Nome', max_length = 194)
    ignicao = models.BooleanField(verbose_name = 'ignicao')
    situacao_movimento = models.BooleanField(verbose_name = 'situacao_movimento' )
    velocidade = models.IntegerField(verbose_name = 'velocidade' )
    latitude = models.FloatField(verbose_name = 'latitude' )
    longitude = models.FloatField(verbose_name = 'longitude' )
    orientacao = models.FloatField(verbose_name = 'orientação' )
    datahora = models.IntegerField(verbose_name = 'data hora' )

    class Meta:
        verbose_name = "dado do rastreamento"
        verbose_name_plural = "dados do rastreamento"

    def __str__(self):
        return self.serial

class resultados_michel(models.Model):
    distancia_percorrida = models.FloatField(verbose_name = 'distancia percorrida' )
    tempo_em_movimento = models.IntegerField(verbose_name = 'Tempo em movimento' )
    tempo_parado = models.IntegerField(verbose_name = 'tempo parado' )
    serial = models.CharField(verbose_name = 'Nome', max_length = 194)


    class Meta:
        verbose_name = "Resultado Michel"
        verbose_name_plural = "Resultados Michel"

    def __str__(self):
        return self.serial