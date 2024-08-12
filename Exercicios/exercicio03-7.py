#6- Crie um método de classe para a conta ClienteBanco.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False 

    def __str__(self):
        return f'Conta de {self.titulo} - Saldo: R$:{self.saldo}'
    
    @classmethod
    def criar_conta(cls, titular, saldo):
        conta = ContaBancaria(titular, saldo)
        return conta

conta_cliente01 = ContaBancaria.criar_conta('Bruna', 10000)