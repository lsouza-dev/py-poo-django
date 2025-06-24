from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=255,blank=False,null=False)
    descricao = models.TextField(max_length=1000,blank=True,null=True)
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome


class Produto (models.Model):
    nome = models.CharField(max_length=255,blank=False,null=False)
    descricao = models.TextField(max_length=1000,blank=True,null=True)
    preco = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0)])
    quantidade_estoque = models.IntegerField(null=False,validators=[MinValueValidator(0)])
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    imagem = models.CharField(null=True,blank=True)
    criado_em = models.DateTimeField(default=timezone.now)
    atualizado_em = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome