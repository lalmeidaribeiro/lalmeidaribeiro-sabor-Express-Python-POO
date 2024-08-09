class Restautante:
    restaurantes = []

    def __init__(self, nome, categoria): #Acessa os atributos da classe realizando qualquer operaçao necessária para inicializar o objeto 
        self._nome = nome.title() #Cria a validação do primeiro caractere em maiusculo 
        self._categoria = categoria.upper()#Deixa todas as letras maiusculas 
        self._ativo = False #_ativo virou um atributo provado
        Restautante.restaurantes.append(self)

    def __str__(self): #Informar o objeto em string/texto. Sem essa def mostratiamos apenas o local da memória Self é a referencia de quem ta chamando a função 
        return f'{self._nome} | {self._categoria}' 

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(23)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(23)} | {restaurante.ativo}')

    @property #Ter a capacidade de pegar um atributo ex: Ativo a forma como é lido 
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    def alternar_estador(self):
        self._ativo = not self._ativo

restaurante_praca = Restautante('Praça', 'Groumet')
restaurante_praca.alternar_estador()
restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
restaurante_manoel = Restautante('Seu Manoel', 'Francesa')

#print(dir(restaurante_praca)) #função dir ele exibe os metodos da clase que está dentro do parametro
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
#print(vars(restaurante_praca))#função que exibe o dicionario da classe

Restautante.listar_restaurantes()