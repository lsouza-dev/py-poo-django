from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer,MatriculaSerializer,ListaMatriculaEstudanteSerializers,ListarMatriculaCursoSerializers,EstudanteSerializerV2
from escola.throttles import MatriculaAnonRateThrottle
from rest_framework import viewsets,generics,filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class EstudanteViewSet(viewsets.ModelViewSet):

    queryset = Estudante.objects.all().order_by("id").order_by("id")
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    search_fields = ['nome','cpf']
    ordering_filters = ['nome']

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer    

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all().order_by("id")
    serializer_class = CursoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]



class MatriculasViewSet(viewsets.ModelViewSet):
    http_method_names = ['get','post']
    queryset = Matricula.objects.all().order_by("id")
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaAnonRateThrottle]

class ListaMatriculaEstudante(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id = self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListaMatriculaEstudanteSerializers


class ListaMatriculaCurso(generics.ListAPIView):

    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk']).order_by("id")
        return queryset
    
    serializer_class = ListarMatriculaCursoSerializers