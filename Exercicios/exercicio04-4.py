'''
    1- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
    Inicie um atributo chamado disponivel como True por padrão.

    2- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano 
    de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    3- Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
    Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

    4- Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e 
    retorna uma lista dos livros disponíveis publicados nesse ano.
                                                  [NÃO RESOLVIDO!]
    '''
class Livro:
    anos = []

    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self.disponivel = True
        Livro.anos.append(self)

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano Publicação: {self._ano_publicado}'
    
    def emprestar(self):
        self.disponivel = False 

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.anos if livro._ano_publicado == ano and livro.disponivel]
        return livros_disponiveis
    
livro01 = Livro('O Matuto', 'Zíbia Gasparetto', 1980)
livro02 = Livro('A volta ao mundo em 80 dias', 'Júlio Verne', 1873)
livro03 = Livro('Python Cookbook', 'Samuel Developer', 2019)
livro04 = Livro("Alice no Pais das Maravilhas", "Samuel Developer", 2019)

livros_disponiveis_2019 = Livro.verificar_disponibilidade(2019)
for livro in livros_disponiveis_2019:
    print(livro)