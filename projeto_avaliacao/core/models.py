from django.db import models

class AlunoModel(models.Model):
    nome = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    ano = models.IntegerField()    

    class Meta:
        verbose_name_plural = 'Alunos'
        verbose_name = 'Aluno'
        
    def __str__(self):
        return self.nome

class Palestra(models.Model):
    palestra = models.CharField(max_length=50)
    palestrantes = models.CharField(max_length=50) 
    curriculo = models.CharField(max_length=200)
    dia_hora = models.DateTimeField()
    sala = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Palestras'
        verbose_name = 'Palestra'
        
    def __str__(self):
        return self.palestra