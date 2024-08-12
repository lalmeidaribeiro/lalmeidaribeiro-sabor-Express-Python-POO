#4- Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
# Utilize propriedades, se necessário.

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
