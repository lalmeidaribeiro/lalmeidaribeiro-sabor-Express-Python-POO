#1- Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
# Inicie o atributo ativo como False por padrão.

class ContaBancario():
    def __init__(self, titulo, saldo=0) -> None:
        self.titulo = titulo
        self.saldo = saldo
        self._ativo = False
        