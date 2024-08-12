#3- Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo 
# ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.
class ContaBancaria():
    def __init__(self, titulo, saldo):
        self.titulo = titulo
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Conta de {self.titulo} - Saldo: R$:{self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
conta01 = ContaBancaria('Joãozinho', 1500)
conta01.ativar_conta()
conta02 = ContaBancaria('Monique', 2000)


conta3 = ContaBancaria("Carlos", 200)
print(f"Antes de ativar: Conta ativa? {conta3._ativo}")
ContaBancaria.ativar_conta(conta3)
print(f"Depois de ativar: Conta ativa? {conta3._ativo}")