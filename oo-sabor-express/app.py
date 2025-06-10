from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça','gourmet')
restaurante_praca.receber_avaliacao('Gui',10)
restaurante_praca.receber_avaliacao('Luiz',8)
restaurante_praca.receber_avaliacao('Helena',2)

def main():
    Restaurante.listar_restaurantes()
    restaurante_praca.media_avaliacoes


if __name__ == '__main__':
    main()