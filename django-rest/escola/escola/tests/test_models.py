from django.test import TestCase
from escola.models import Estudante,Matricula,Curso

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'teste@gmail.com',
            cpf = '74023201030',
            data_nascimento = '2023-02-02',
            celular = '27 99999-9988'
        )
    
    def test_verifica_atributos_de_estudante(self):
        '''
        Teste que verifica os atributos do modelo de Estudante
        '''
        
        self.assertEqual(self.estudante.nome,'Teste de Modelo')
        self.assertEqual(self.estudante.email ,'teste@gmail.com',)
        self.assertEqual(self.estudante.cpf,'74023201030')
        self.assertEqual(self.estudante.data_nascimento,'2023-02-02')
        self.assertEqual(self.estudante.celular,'27 99999-9988')
        
class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = 'CPOO01',
            descricao = 'Curso de Programação Orientada a Objetos nº 1',
            nivel = 'B'
        )
    
    def test_verifica_atributos_curso(self):
        self.assertEqual(self.curso.codigo,'CPOO01')
        self.assertEqual(self.curso.descricao,'Curso de Programação Orientada a Objetos nº 1')
        self.assertEqual(self.curso.nivel,'B')
        
class ModelMatriculaCaseTest(TestCase):
    def setUp(self):
        
        self.estudante = Estudante.objects.create(
            nome = 'Teste de Modelo',
            email = 'teste@gmail.com',
            cpf = '74023201030',
            data_nascimento = '2023-02-02',
            celular = '27 99999-9988'
        )
        
        self.curso = Curso.objects.create(
            codigo = 'CPOO01',
            descricao = 'Curso de Programação Orientada a Objetos nº 1',
            nivel = 'B'
        )
        
        self.matricula = Matricula.objects.create(
            estudante = self.estudante,
            curso = self.curso,
            periodo = 'M'
        )
        
    def test_verifica_atributos_matricula(self):
        self.assertEqual(self.matricula.estudante,self.estudante)
        self.assertEqual(self.matricula.curso,self.curso)
        self.assertEqual(self.matricula.periodo,'M')