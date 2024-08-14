from modelos.restaurante import Restautante

restaurante_praca = Restautante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Lari', 10)
restaurante_praca.receber_avaliacao('Bru',8)
restaurante_praca.receber_avaliacao('JJ',2)

restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
restaurante_pizza.receber_avaliacao('Lele', 5)
restaurante_pizza.receber_avaliacao('Tata',8)
restaurante_pizza.receber_avaliacao('Ju',3)

restaurante_manoel = Restautante('Seu Manoel', 'Francesa')
restaurante_manoel.receber_avaliacao('Lele', 7)
restaurante_manoel.receber_avaliacao('Tata',10)
restaurante_manoel.receber_avaliacao('Ju',10)

restaurante_praca.alternar_estador()
restaurante_manoel.alternar_estador()

def main():
    Restautante.listar_restaurantes()

if __name__ == '__main__':
    main()