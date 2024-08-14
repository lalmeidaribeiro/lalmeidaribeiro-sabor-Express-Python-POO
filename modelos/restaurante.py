from modelos.avaliacao import Avaliacao

class Restautante:
    """Representa um restaurante e suas características."""

    restaurantes = []

    def __init__(self, nome, categoria): #Acessa os atributos da classe realizando qualquer operaçao necessária para inicializar o objeto 
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """

        self._nome = nome.title() #Cria a validação do primeiro caractere em maiusculo 
        self._categoria = categoria.upper()#Deixa todas as letras maiusculas 
        self._ativo = False #_ativo virou um atributo provado
        self._avaliacao = []
        Restautante.restaurantes.append(self)

    def __str__(self): #Informar o objeto em string/texto. Sem essa def mostratiamos apenas o local da memória Self é a referencia de quem ta chamando a função 
        """Retorna uma representação em string do restaurante."""

        return f'{self._nome} | {self._categoria}' 

    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""

        print(f'{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(23)} | {'Avaliação'.ljust(23)} | {'Status'}\n')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(23)} | {str(restaurante.media_avaliacoes).ljust(23)} | {restaurante.ativo}')

    @property #Ter a capacidade de pegar um atributo ex: Ativo a forma como é lido 
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante."""
        return '✔️' if self._ativo else '❌'
    
    def alternar_estador(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo

    def  receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        

    @property 
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas/quantidade_de_notas,1)
        return media



#print(dir(restaurante_praca)) #função dir ele exibe os metodos da clase que está dentro do parametro
#print(restaurante_praca.ativo) #Busca uma variavel da classe 
#print(vars(restaurante_praca))#função que exibe o dicionario da classe

#Restautante.listar_restaurantes()