class Restautante:
    def __init__(self, nome, categoria): #Acessa os atributos da classe realizando qualquer operaçao necessária para inicializar o objeto 
        self.nome = nome 
        self.categoria = nome
        self. ativo = False

restaurante_praca = Restautante('Praça', 'Groumet')
restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
restaurante_manoel = Restautante('Seu Manoel', 'Francesa')


lista_restaurantes = [restaurante_praca,restaurante_pizza, restaurante_manoel]

#print(dir(restaurante_praca)) #função dir ele exibe os metodos da clase que está dentro do parametro
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
print(vars(restaurante_praca))#função que exibe o dicionario da classe
print(vars(restaurante_pizza))
print(vars(restaurante_manoel))