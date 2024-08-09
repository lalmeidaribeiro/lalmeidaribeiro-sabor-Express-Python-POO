#Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, 
# seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.

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