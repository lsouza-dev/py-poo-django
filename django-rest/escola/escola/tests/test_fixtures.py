from django.test import TestCase
from escola.models import Estudante,Curso

class FixturesTestCase(TestCase):
    fixtures = ['prototipo_banco.json']
    
    
    def test_carregamento_da_fixtures(self):
        '''
        Teste que verifica o carregamento da fixture
        '''
        
        estudante = Estudante.objects.get(cpf = '19818458796')
        curso = Curso.objects.get(pk=1)
        self.assertEqual(estudante.celular,'27992036558')
        self.assertEqual(curso.codigo,'POO')