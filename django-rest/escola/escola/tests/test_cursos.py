from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursoTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    
    def setUp(self):
        # self.usuario = User.objects.create_superuser(
        #     username='admin',
        #     password='admin'
        # )
        
        self.usuario = User.objects.get(username = 'lsouza.dev')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        
        # self.curso_01 = Curso.objects.create(
        #     codigo = 'ABC001',
        #     descricao = 'Curso de Teste 001',
        #     nivel = 'I'
        # )
        
        # self.curso_02 = Curso.objects.create(
        #     codigo = 'ABC002',
        #     descricao = 'Curso de Teste 002',
        #     nivel = 'A'
        # )
        
        
        self.curso_01 = Curso.objects.get(pk=1)
        self.curso_02 = Curso.objects.get(pk=2)
        
    def test_requisicao_get_cursos_list(self):
    
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        
    def test_requisicao_get_um_curso(self):
        self.curso = Curso.objects.create(
            codigo = 'CDRF01',
            descricao = 'Curso de desenvolvimento com Django Rest Framework',
            nivel = 'A'
        )
        
        response = self.client.get(self.url + '1/')
        dados_curso = Curso.objects.get(pk=1)
        dados_curso_serializado = CursoSerializer(instance = dados_curso).data
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,dados_curso_serializado)
        
    def test_requisico_post_curso(self):
        dados = {
            'codigo' : 'CDRF01',
            'descricao' : 'Curso de desenvolvimento com Django Rest Framework',
            'nivel' : 'A'
        }
        
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_requisicao_delete_um_estudante(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)