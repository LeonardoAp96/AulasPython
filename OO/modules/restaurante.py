from modules.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    
    def __init__(self, nome, categoria):
        ''' Precisa de dois argumentos '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) #insere o restaurante na lista
    
    #o 'self' não é uma palavra reservada, referencia ao proprio objeto chamado
    def __str__(self):
        ''' Retorna o nome|categoria do objeto'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'avaliacao'.ljust(20)} {'ativo'.ljust(20)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} {restaurante.ativo}')
            
    @property
    def ativo(self):
        '''usado coolsymbols'''
        return "verdade✩" if self._ativo else "mentira"
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quant_de_notas, 1)
        return media
    
