#5- Crie uma instância da classe e imprima o valor da propriedade titular.

class ContaBancaria():
    def __init__(self, titulo, saldo):
        self._titulo = titulo
        self._saldo = saldo
        self._ativo = False
    @property
    def titulo(self):
        return self._titulo

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
conta4 = ContaBancaria("Fernanda", 1500)
print(f"Titular da conta 4: {conta4._titulo}")