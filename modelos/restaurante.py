from modelos.avaliacao import Avaliacao

class Restautante:
    restaurantes = []

    def __init__(self, nome, categoria): #Acessa os atributos da classe realizando qualquer operaçao necessária para inicializar o objeto 
        self._nome = nome.title() #Cria a validação do primeiro caractere em maiusculo 
        self._categoria = categoria.upper()#Deixa todas as letras maiusculas 
        self._ativo = False #_ativo virou um atributo provado
        self._avaliacao = []
        Restautante.restaurantes.append(self)

    def __str__(self): #Informar o objeto em string/texto. Sem essa def mostratiamos apenas o local da memória Self é a referencia de quem ta chamando a função 
        return f'{self._nome} | {self._categoria}' 

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(23)} | {'Avaliação'.ljust(23)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(23)} | {str(restaurante.media_avaliacoes).ljust(23)} | {restaurante.ativo}')

    @property #Ter a capacidade de pegar um atributo ex: Ativo a forma como é lido 
    def ativo(self):
        return '✔️' if self._ativo else '❌'
    
    def alternar_estador(self):
        self._ativo = not self._ativo

    def  receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property 
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas,1)
        return media



#print(dir(restaurante_praca)) #função dir ele exibe os metodos da clase que está dentro do parametro
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
#print(vars(restaurante_praca))#função que exibe o dicionario da classe

#Restautante.listar_restaurantes()