class ContaBancaria:
    def __init__(self, titular = '', saldo = 0.0, ativo = False):
        self.titular = titular
        self.saldo = saldo
        self._ativo = ativo
    
    def __str__(self):
        return f'{self.titular} - Saldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(self):
        self._ativo = True

    

contaBancaria1 = ContaBancaria('lol', 4)
contaBancaria2 = ContaBancaria('gog',5)

print(contaBancaria1)

contaBancaria1.ativar_conta()
