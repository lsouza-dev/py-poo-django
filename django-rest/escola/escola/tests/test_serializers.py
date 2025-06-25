from django.test import TestCase
from escola.models import Estudante,Curso,Matricula
from escola.serializers import EstudanteSerializer,EstudanteSerializerV2,CursoSerializer,MatriculaSerializer

class SerializerEstudanteTestCase(TestCase):
    def setUp(self):
         self.estudante = Estudante(
            nome = 'Teste de Modelo',
            email = 'teste@gmail.com',
            cpf = '74023201030',
            data_nascimento = '2023-02-02',
            celular = '27 99999-9988'
        )
         
         self.serializer_estudante = EstudanteSerializer(instance = self.estudante)
         
    def test_verifica_campos_serializados_de_estudante(self):
        '''
        Teste que verifica os campos que estão sendo serializados de estudante
        '''
        
        dados = self.serializer_estudante.data
        self.assertEqual(set(dados.keys()),set(['id','nome','email','cpf','data_nascimento','celular']))
    
    def test_verifica_conteudo_dos_campos_serializados_de_estudante(self):
        '''
        Teste que verifica os campos que estão sendo serializados de estudante
        '''
        
        dados = self.serializer_estudante.data
        
        self.assertEqual(dados['nome'],self.estudante.nome)
        self.assertEqual(dados['email'],self.estudante.email)
        self.assertEqual(dados['cpf'],self.estudante.cpf)
        self.assertEqual(dados['data_nascimento'],self.estudante.data_nascimento)
        self.assertEqual(dados['celular'],self.estudante.celular)
        
class SerializerCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CPOO01',
            descricao = 'Curso de Programação Orientada a Objetos nº 1',
            nivel = 'B'
        )
        
        self.serializer_curso = CursoSerializer(instance=self.curso)
        
    def test_verifica_campos_curso_serializer(self):
        '''
        Teste que verifica os campos serializados na classe de Curso
        '''
        
        dados = self.serializer_curso.data
        
        self.assertEqual(set(dados.keys()),set(['id','codigo','descricao','nivel']))
        
    def test_verifica_valores_dos_campos_curso_serializer(self):
        '''
        Teste que verifica os dados retornados nos campos dos serializers de curso
        '''
        
        dados = self.serializer_curso.data
        self.assertEqual(dados['codigo'],self.curso.codigo)
        self.assertEqual(dados['descricao'],self.curso.descricao)
        self.assertEqual(dados['nivel'],self.curso.nivel)
        
class SerializerMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante(
            nome = 'Luiz Fabiano de Souza',
            email = 'luizfabiano@gmail.com',
            cpf = '32177253012',
            data_nascimento = '2024-05-24',
            celular = '27 99999-1234'
        )   
        
        self.curso = Curso(
            codigo = 'CDA01',
            descricao = 'Curso de Django Avançado 01',
            nivel = 'A'
        )
        
        self.matricula = Matricula(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'N'
        )
        
        self.serializer_matricula = MatriculaSerializer(instance=self.matricula)
        
        
    def test_verifica_campos_serializer_matricula(self):
        '''
        Teste que verifica os campos serializados de matrículas
        '''
        
        dados = self.serializer_matricula.data
        
        self.assertEqual(set(dados.keys()),set(['id','estudante','curso','periodo']))
        
    def test_verifica_valores_dos_campos_serializer_matricula(self):
        '''
        Teste que verifica os valores retornados nos campos do serializer de matricula
        '''
        
        dados = self.serializer_matricula.data
        
        self.assertEqual(dados['estudante'],self.matricula.estudante.id)
        self.assertEqual(dados['curso'],self.matricula.curso.id)
        self.assertEqual(dados['periodo'],self.matricula.periodo)
        