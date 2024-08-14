from modelos.restaurante import Restautante

restaurante_praca = Restautante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Lari', 10)
restaurante_praca.receber_avaliacao('Bru',8)
restaurante_praca.receber_avaliacao('JJ',2)

#restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
#restaurante_manoel = Restautante('Seu Manoel', 'Francesa')

#restaurante_pizza.alternar_estador()

def main():
    Restautante.listar_restaurantes()

if __name__ == '__main__':
    main()