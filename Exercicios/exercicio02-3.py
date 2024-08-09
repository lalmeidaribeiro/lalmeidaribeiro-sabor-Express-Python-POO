#3- Modifique a classe Restaurante adicionando um construtor que aceita nome e 
# categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
class Restaurante():
    def __init__(self, nome, categoria, entrega, ativo = False, unidades = 0):
        self.nome = nome 
        self.categoria  = categoria 
        self.entrega = entrega
        self.ativo = ativo
        self.unidades = unidades

   # def __str__(self):
    #   return f'Restaurante: {self.nome}\nCategoria: {self.categoria}\nfaz entre? {self.entrega}\nPossui unidades? {self.unidades}\nEstá ativo? {self.ativo}'

#restaurante_larissa = Restaurante('Larissas Restaurant', 'Brasileiro','Sim', True, 10)
restaurante_larissa02 = Restaurante(nome ='Larissa Restaurant2', categoria ='Fasr Food')

#print(restaurante_larissa02)