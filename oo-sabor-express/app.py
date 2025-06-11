from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa


restaurante_praca = Restaurante('praça','gourmet')
bebida_suco = Bebida('Suco de Melancia',5.0,'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho',2.0,'O melhor pão da cidade!')
prato_paozinho.aplicar_desconto()
sobremesa_pudim = Sobremesa('Pudim',20,'PUDIM GOSTOSO DEMAIS DE DOCE DE LEITE')
sobremesa_pudim.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(sobremesa_pudim)


class Banco:
    def __init__(self,nome,endereco):
        self._nome = nome
        self._endereco = endereco
    
    def __str__(self):
        return f'{self._nome} - {self._endereco}'
    
class Agencia(Banco):
    def __init__(self,nome,endereco,numero):
        super().__init__(nome,endereco)
        self._numero = numero

    def __str__(self):
        return f'{super().__str__()} - {self._numero}'

banco = Banco('Banco do Brasil','Vitória')
agencia = Agencia('BB Serra','Serra',231)


def main():
    print(bebida_suco)
    print(prato_paozinho)
    print(banco)
    print(agencia)

    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
