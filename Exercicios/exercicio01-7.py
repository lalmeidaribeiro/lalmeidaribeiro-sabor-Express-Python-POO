#7- Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.
class Restautante:
    nome = '' 
    categoria = ''
    ativo = False

restaurante_pizza = Restautante()  
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

if restaurante_pizza.categoria == 'Fast Food':
    print(f'A categoria do restaurante {restaurante_pizza.nome} é Fast Food')
else:
    print(f'A categoria do restaurante {restaurante_pizza.nome} não é Fast Food')