'''No Python, a criação de classes é uma parte essencial da programação orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:

class Musica:
    nome = ''
    artista = ''
    duracao = int
Copiar código
Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.'''

class Musica:

    def __init__(self, nome, artista,duracao = 0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}' 

musica1 = Musica('Pontos de exclamação','Vintage Culture',150)
musica2 = Musica('Vacilão','Revelação',10)
musica3 = Musica('Camarão que dorme a onda leva','Beth Carvalho',20)



print(f'{musica1}\n{musica2}\n{musica3}')