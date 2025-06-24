from rest_framework import serializers
from meteora.models import Categoria,Produto

class ProdutoSerializer(serializers.ModelSerializer):
    preco = serializers.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        model = Produto

        fields = ['nome',
            'descricao',
            'preco',
            'quantidade_estoque',
            'categoria',
            'imagem',
            'criado_em',
            'atualizado_em']


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'