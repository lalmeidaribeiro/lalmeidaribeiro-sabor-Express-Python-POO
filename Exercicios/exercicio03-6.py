#6- Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. 
# Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

class ClienteBanco:
    def __init__(self, nome, sobrenome, cpf, saldo, status):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf
        self.saldo = saldo
        self.status = status

    def __str__(self,nome, sobrenome, cpf, saldo, status):
        return f'O nome do titular da conta é: {self._nome} {self._sobrenome}. CPF: {self._cpf}, Sua conta possui R$: {self.saldo} e se encontra {self.status}'

conta01 = ClienteBanco('Larissa', 'Ribeiro', 35949048536, 5000, 'Ativo')      
conta02 = ClienteBanco('Leticia', 'Ribeiro', 35307589039, 10000, 'Ativo')     
conta03 = ClienteBanco('Marcos', 'Vinicius', 35058580029, 3000, 'Ativo')    
