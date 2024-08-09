#1- Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
# Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    def __init__(self, modelo, cor, ano = 0):
        self.modelo = modelo 
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'Modelo: {self.modelo} |Cor: {self.cor} |Ano: {self.ano}'

carro_larissa = Carro('Jeep Troller', 'Vermelha', 2020)
carro_letiica = Carro('Volkswagem Amarok', 'Cinza',2020)

print(carro_larissa)