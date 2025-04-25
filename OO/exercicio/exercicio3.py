class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

#-------------------------------------------------------------------------------

class Veiculo:
    def __init__(self, marca, modelo):
        '''classe Veiculo, precisa de marca e modelo'''
        self._marca = marca
        self._modelo = modelo
        self._ligado = False
    
    @property
    def ligado(self):
        ''' retorna se esta ligado ou não'''
        return 'ligado' if self._ligado else 'desligado'

    def __str__(self):
        return f'Marca: {self._marca.ljust(5)}| Modelo: {self._modelo.ljust(5)}| {self.ligado}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        '''classe Carro, precisa tambem de portas'''
        super().__init__(marca, modelo)
        self._portas = portas

    def __str__(self):
        return f'{super().__str__().ljust(5)} | Portas: {self._portas}'

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        '''Moto, precisa do tipo esportiva/casual'''
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} | Tipo: {self._tipo}' 

carro1 = Carro('fiat', 'uno', 2)
moto1 = Moto('fiat', 'uno', 'esportiva')

print(f'{carro1}')
    
