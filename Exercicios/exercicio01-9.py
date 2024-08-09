#9- Imprima no console o nome e a categoria da instância restaurante_praca.

class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_praca = Restautante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

print(f'O nome do restaurante é: {restaurante_praca.nome} e sua categoria é: {restaurante_praca.categoria}')