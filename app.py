from modelos.restaurante import Restautante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restautante('Praça', 'Gourmet')
#restaurante_praca.receber_avaliacao('Lari', 10)
#restaurante_praca.receber_avaliacao('Bru',8)
#restaurante_praca.receber_avaliacao('JJ',2)
restaurante_praca = bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
restaurante_praca = prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
 


restaurante_pizza = Restautante('Pizza Express', 'Italiana')  
#restaurante_pizza.receber_avaliacao('Lele', 5)
#restaurante_pizza.receber_avaliacao('Tata',8)
#restaurante_pizza.receber_avaliacao('Ju',3)

restaurante_manoel = Restautante('Seu Manoel', 'Francesa')
#restaurante_manoel.receber_avaliacao('Lele', 7)
#restaurante_manoel.receber_avaliacao('Tata',10)
#restaurante_manoel.receber_avaliacao('Ju',10)

#restaurante_praca.alternar_estador()
#restaurante_manoel.alternar_estador()


def main():
    #Restautante.listar_restaurantes()
    print(bebida_suco)
    print(prato_paozinho)
if __name__ == '__main__':
    main()