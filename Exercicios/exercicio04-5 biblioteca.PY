'''
    5- Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
'''
from Exercicios.exercicio04Livros import Livro

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

livro01.emprestar()

