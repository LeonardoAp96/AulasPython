class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        ''' Precisa de dois argumentos '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) #insere o restaurante na lista
    
    #o 'self' não é uma palavra reservada, referencia ao proprio objeto chamado
    def __str__(self):
        ''' Retorna o nome|categoria do objeto'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {restaurante.ativo}')
            
    @property
    def ativo(self):
        '''usado coolsymbols'''
        return "verdade✩" if self._ativo else "mentira"
    
    def alternar_estado(self):
        self._ativo = not self._ativo
        

    
restaurante_praca = Restaurante('Praca', 'gourmet')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza', 'frfr')


Restaurante.listar_restaurantes()
