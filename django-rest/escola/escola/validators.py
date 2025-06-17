from validate_docbr import CPF
import re

def cpf_invalido(cpf):
        validator_cpf = CPF()
        valido = validator_cpf.validate(cpf)
        return not valido

def nome_invalido(nome):
        return not nome.isalpha()

def celular_invalido(celular):
        #12 12332-2132
        modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
        resposta = re.findall(modelo,celular)
        print(resposta)
        return not resposta
        # return len(celular) != 13
