from modules.restaurante import Restaurante

restaurante_praca = Restaurante('Praca', 'gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza', 'frfr')

restaurante_praca.receber_avaliacao('gui', 3)
restaurante_praca.receber_avaliacao('anna', 10)
restaurante_praca.receber_avaliacao('joi', 3)



def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()