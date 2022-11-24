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