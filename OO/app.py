from modules.restaurante import Restaurante
from modules.cardapio.bebida import Bebida
from modules.cardapio.prato import Prato

restaurante_praca = Restaurante('Praca', 'gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza', 'frfr')
restaurante_praca.receber_avaliacao('gui', 3)
restaurante_praca.receber_avaliacao('anna', 10)
restaurante_praca.receber_avaliacao('joi', 3)

bebida1 = Bebida('suco de melancia', 4.0, 'medio')
prato1 = Prato('mamao', 1, 'mamamooo')



def main():
    Restaurante.listar_restaurantes()
    print(bebida1)
    print(prato1)

if __name__ == '__main__':
    main()
