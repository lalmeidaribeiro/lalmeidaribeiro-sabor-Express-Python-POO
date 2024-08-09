'''Em programação orientada a objetos (OO), uma classe é um modelo para criar objetos. Um objeto é uma instância específica de uma classe, e as classes são utilizadas para definir o comportamento e as propriedades compartilhadas por um grupo de objetos relacionados.

Por exemplo, uma classe Música poderia ter 3 atributos (que trazem as características ou propriedades de um objeto):

nome
artista
duracao
Copiar código
Agora é sua vez! Crie uma classe chamada Musica com os seguintes atributos e crie 3 objetos definindo cada atributo..'''

class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Pontos de exclamação'
musica1.artista = 'Vintage Culture'
musica1.duracao = 150

musica2 = Musica()
musica2.nome = 'Vacilão'
musica2.artista = 'Revelação'
musica2.duracao = 3

musica3 = Musica()
musica3.nome = 'Camarão que dorme a onda leva'
musica3.artista = 'Beth Carvalho'
musica3.duracao = 10