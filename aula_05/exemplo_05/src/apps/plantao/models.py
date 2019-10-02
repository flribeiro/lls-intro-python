from django.db import models


class Area(models.Model):
    nome = models.CharField(max_length=70)

    def __str__(self):
        return self.nome


class Plantonista(models.Model):
    área = models.ForeignKey(Area, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Contato', max_length=20)
    observação = models.CharField('Observação', max_length=40)

    def __str__(self):
        return self.nome
