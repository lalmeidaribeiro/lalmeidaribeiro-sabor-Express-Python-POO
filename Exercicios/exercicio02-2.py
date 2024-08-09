#2- Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
# Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante():
    def __init__(self, nome, categoria, entrega, ativo = False, unidades = 0):
        self.nome = nome 
        self.categoria  = categoria 
        self.entrega = entrega
        self.ativo = ativo
        self.unidades = unidades

    def __str__(self):
       return f'Restaurante: {self.nome}\nCategoria: {self.categoria}\nfaz entre? {self.entrega}\nPossui unidades? {self.unidades}\nEstá ativo? {self.ativo}'

restaurante_larissa = Restaurante('Larissas Restaurant', 'Brasileiro','Sim', True, 10)

print(restaurante_larissa)