from modelos.cardapio.item_cardapio import ItemCardapio
class Sobremesa(ItemCardapio):
    def __init__(self,nome,preco,descricao):
        super().__init__(nome,preco)
        self._descricao = descricao
    
    def __str__(self):
        return f'{super().__str__(self)} - Descricao: {self._descricao}'
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * .02)