#2- Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_praca = Restautante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

print(restaurante_praca.nome)