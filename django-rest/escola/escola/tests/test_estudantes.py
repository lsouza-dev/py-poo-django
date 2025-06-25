from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Estudante
from escola.serializers import EstudanteSerializer


class EstudantesTestCase(APITestCase):
    fixtures = ['prototipo_banco.json']
    
    def setUp(self):
        # self.usuario = User.objects.create_superuser(
        #     username='admin',
        #     password='admin'
        # )
        self.usuario = User.objects.get(username = 'lsouza.dev')
        self.url = reverse('Estudantes-list')
        self.client.force_authenticate(user=self.usuario)
        
        # self.estudante_01 = Estudante.objects.create(
        #     nome = 'Teste estudante um',
        #     email = 'testeestudanteum@gmail.com',
        #     cpf = '72121878017',
        #     data_nascimento = '2024-01-02',
        #     celular = '87 99999-2312'
        # )
        
        # self.estudante_02 = Estudante.objects.create(
        #     nome = 'Teste estudante dois',
        #     email = 'testeestudante1@gmail.com',
        #     cpf = '92222443032',
        #     data_nascimento = '2024-01-02',
        #     celular = '87 99999-2312'
        # )
    
        self.estudante_01 = Estudante.objects.get(pk=1)
        self.estudante_02 = Estudante.objects.get(pk=2)
    
    def test_requisicao_get_para_listar_estudantes(self):
        '''
        Teste de requisição get
        '''
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    
    def test_requisicao_get_para_listar_um_estudante(self):
        '''
        Teste de requisição get para um estudante
        '''
        
        response = self.client.get(self.url + '1/')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
        dados_estudante = Estudante.objects.get(pk=1)
        dados_estudante_serializados = EstudanteSerializer(instance = dados_estudante).data
        self.assertEqual(response.data,dados_estudante_serializados)        
        # self.assertEqual()
        
        
    
    def test_requisicao_post_para_criar_um_estudante(self):
        '''
        Teste de requisição post para o estudante
        '''
        dados = {
            'nome' : 'Luiz',
            'email' : 'testePOST@gmail.com',
            'cpf' : '52950040071',
            'data_nascimento' : '2024-01-02',
            'celular' : '11 99999-9999'
        }
        response = self.client.post(self.url, dados)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
    
    def test_requisicao_delete_um_curso(self):
        response = self.client.delete(f'{self.url}2/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
        
        
    def test_requisicao_put_para_atualizar_um_estudante(self):
        '''
        Teste de requisição put para o estudante
        '''
        dados = {
            'nome' : 'Luiz Fabiano de Souza',
            'email' : 'testePUT@gmail.com',
            'cpf' : '68736398004',
            'data_nascimento' : '2024-01-02',
            'celular' : '11 99999-9999'
        }
        
        response = self.client.put(f'{self.url}2/',data= dados)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        
    