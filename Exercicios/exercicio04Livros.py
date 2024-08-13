'''
    1- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
    Inicie um atributo chamado disponivel como True por padrão.

    2- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano 
    de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.
    '''
class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self.disponivel = True

    def __str__(self):
        return f'Livro: {self._titulo} | Autor: {self._autor} | Ano Publicação: {self._ano_publicado}'

livro01 = Livro('O Matuto', 'Zíbia Gasparetto', 1980)
livro02 = Livro('A volta ao mundo em 80 dias', 'Júlio Verne', 1873)

print(livro01)
print(livro02)