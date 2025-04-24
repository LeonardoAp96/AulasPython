class Carro:
    def __init__(self, modelo = '', cor = 'branco'):
        ''' Precisa de dois argumentos'''
        self.modelo = modelo
        self.cor = cor
        self.ano = 2000

carro = Carro('Fiat', 9)
carro2 = Carro()

print(carro.cor)


class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Ola {self.nome}, trabalho com {self.profissao}'
        else:
            return f'Ola {self.nome}'

# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)
print()

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.aniversario()
pessoa3.aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)
print()

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)
