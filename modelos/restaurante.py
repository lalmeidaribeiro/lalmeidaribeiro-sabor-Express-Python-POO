class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_praca = Restautante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restautante()  
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

restauranteManoel = Restautante()
restauranteManoel.nome = 'Seu Manoel Massas'
restauranteManoel.categoria = 'Italiana'
restauranteManoel.ativo = True

lista_restaurantes = [restaurante_praca,restaurante_pizza, restauranteManoel]

#print(dir(restaurante_praca)) #função dir ele exibe os atributos do objeto
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
print(vars(restaurante_praca))#função que exibe o dicionario da classe