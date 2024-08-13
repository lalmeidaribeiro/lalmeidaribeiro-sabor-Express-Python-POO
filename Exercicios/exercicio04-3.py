'''
    1- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
    Inicie um atributo chamado disponivel como True por padrão.

    2- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano 
    de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

    3- Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
    Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
    '''
class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self.disponivel = True

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano Publicação: {self._ano_publicado}'
    
    def emprestar(self):
        self.disponivel = False 

livro3 = Livro("Python Cookbook", "Samuel Developer", 2019)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")
