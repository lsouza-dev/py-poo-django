from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula,Curso,Estudante
from escola.serializers import MatriculaSerializer

class MatriculasTestCase(APITestCase):
    
    fixtures = ['prototipo_banco.json']
    def setUp(self):
        # self.usuario = User.objects.create_superuser(
        #     username='admin',
        #     password='admin'
        # )
        
        self.usuario = User.objects.get(username ='lsouza.dev')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        
    def test_requisicao_get_matriculas_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        
    def test_requisicao_get_uma_matricula(self):
        
        # self.estudante = Estudante.objects.create(
        #     nome = 'Luiz',
        #     email = 'testePOST@gmail.com',
        #     cpf = '52950040071',
        #     data_nascimento = '2024-01-02',
        #     celular = '11 99999-9999'
        # )
        
        # self.curso = Curso.objects.create(
        #     codigo = 'CP001',
        #     descricao = 'Curso de Programação 001',
        #     nivel = 'B'
        # )
        
        # self.matricula = Matricula.objects.create(
        #     estudante = self.estudante,
        #     curso = self.curso,
        #     periodo = 'M'
        # )
        self.estudante = Estudante.objects.get(pk=1)
        self.curso = Curso.objects.get(pk=1)
        self.matricula = Matricula.objects.get(pk=1)
        
        response = self.client.get(self.url + '1/')
        dados_matricula = Matricula.objects.get(pk=1)
        dados_matricula_serializados = MatriculaSerializer(dados_matricula).data
        self.assertEqual(response.data,dados_matricula_serializados)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    def test_requisicao_post_matricula(self):
        
        self.estudante = Estudante.objects.create(
            nome = 'Luiz',
            email = 'testePOST@gmail.com',
            cpf = '52950040071',
            data_nascimento = '2024-01-02',
            celular = '11 99999-9999'
        )
        
        self.curso = Curso.objects.create(
            codigo = 'CP001',
            descricao = 'Curso de Programação 001',
            nivel = 'B'
        )
        
        dados = {
            'estudante' : self.estudante.pk,
            'curso' : self.curso.pk,
            'periodo' : 'M'
        }
        
        response = self.client.post(self.url,dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        
    def test_requisicao_delete_uma_matricula(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_405_METHOD_NOT_ALLOWED)