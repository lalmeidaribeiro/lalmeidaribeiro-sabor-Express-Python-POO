'''
Quarta Lista de exercício:
    1- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. 
    Inicie um atributo chamado disponivel como True por padrão.
'''
class Livro:
    def __init__(self, titulo, autor, ano_publicado):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self.disponivel = True


        