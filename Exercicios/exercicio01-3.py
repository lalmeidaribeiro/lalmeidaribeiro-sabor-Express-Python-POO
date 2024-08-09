#3- Verifique o valor inicial do atributo ativo para a instância restaurante_praca
#  e exiba uma mensagem informando se o restaurante está ativo ou inativo.

class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_praca = Restautante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_praca.ativo = False

if restaurante_praca.ativo == True:
    print(f'O restaurante {restaurante_praca.nome} está com o status Ativo!')
else:
    print(f'O restaurante {restaurante_praca.nome} está com o status Inativo!')