from django.db import models
from datetime import date
# Create your models here.

class Livros(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 30)
    co_autor = models.CharField(max_length = 30)
    data_registo = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(blank = True, max_length = 30)
    data_emprestimo = models.DateTimeField(null = True, blank = True)
    data_devolucao = models.DateTimeField(null = True, blank = True)
    tempo_duracao = models.DateField(null = True, blank = True)
    
    class Meta:
        verbose_name = "Livro"
        
    def __str__(self):
        return self.nome