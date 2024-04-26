# models.py

from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    ano_publicacao = models.IntegerField()
    genero = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    disponibilidade = models.BooleanField(default=True)

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_devolucao = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False)