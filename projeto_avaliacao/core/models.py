from django.db import models

class AlunoModel(models.Model):
    nome = models.CharField(default=..., max_length=50)
    curso = models.CharField(max_length=50)
    ano = models.IntegerField()    
