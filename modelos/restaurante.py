class Restautante:
    restaurantes = []

    def __init__(self, nome, categoria): #Acessa os atributos da classe realizando qualquer operaçao necessária para inicializar o objeto 
        self.nome = nome 
        self.categoria = categoria
        self.ativo = False
        Restautante.restaurantes.append(self)

    def __str__(self): #Informar o objeto em string/texto. Sem essa def mostratiamos apenas o local da memória Self é a referencia de quem ta chamando a função 
        return f'{self.nome} | {self.categoria}' 

    def listar_restaurantes():
        for restaurante in Restautante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restautante('Praça', 'Groumet')
restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
restaurante_manoel = Restautante('Seu Manoel', 'Francesa')

#print(dir(restaurante_praca)) #função dir ele exibe os metodos da clase que está dentro do parametro
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
#print(vars(restaurante_praca))#função que exibe o dicionario da classe

Restautante.listar_restaurantes()