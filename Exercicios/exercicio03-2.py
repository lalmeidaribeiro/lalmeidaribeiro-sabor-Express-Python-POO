#2- Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem 
# formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.
class ContaBancaria():
    def __init__(self, titulo, saldo):
        self.titulo = titulo
        self.saldo = saldo
        self._ativo = False
    
    def __str__(self):
        return f'Conta de {self.titulo} - Saldo: R$:{self.saldo}'
    
conta01 = ContaBancaria('Joãozinho', 1500)
conta02 = ContaBancaria('Monique', 2000)

print(conta01)
print(conta02)
