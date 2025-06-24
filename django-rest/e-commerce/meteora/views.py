from rest_framework import viewsets,filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from meteora.models import Produto,Categoria
from meteora.serializers import ProdutoSerializer,CategoriaSerializer

class ProdutoView(viewsets.ModelViewSet):
    queryset = Produto.objects.all().order_by('id')
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['id','nome','categoria__id','categoria__nome','quantidade_estoque']
    ordering_fields = ['nome','categoria__id','preco']
    
    

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all().order_by('id')
    serializer_class = CategoriaSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['nome','id']
    ordering_fields = ['nome','criado_em','atualizado_em']