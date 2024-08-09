#5- Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe
#  e atribua valores aos seus atributos através de um método construtor.

class Cliente():
    clientes = []
    def __init__(self,nome, profissao, hobby, idade = 0):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.hobby = hobby
        Cliente.clientes.append(self)

    def __str__(self):
        return f'Nome:{self.nome}|Profissão: {self.profissao} |Hobby: {self.hobby} |Idade:{self.idade} '
    
    def lista_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome: {cliente.nome}|Profissão: {cliente.profissao} |Hobby: {cliente.hobby} |Idade: {cliente.idade}')

cliente_larissa = Cliente('Larissa Ribeiro','Analista de TI','Natação',20)
cliente_leticia = Cliente('Leticia Ribeiro','Design Gráfico e Marketing Digital','Natação',20)
cliente_luiz = Cliente('José Luiz','Aposentado','Culinária',60)

Cliente.lista_clientes()
