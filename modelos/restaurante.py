class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_praca = Restautante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restautante()  

lista_restaurantes = [restaurante_praca,restaurante_pizza]

#print(dir(restaurante_praca)) #função dir ele exibe os atributos do objeto
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
print(vars(restaurante_praca))#função que exibe o dicionario da classe