from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): #Herdando informações da classe ItemCardapio
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) #'super' objeto especial, que permite acessar informações de outra classe
        self.descricao = descricao #estou criando a descrição da clase Prato
    
    def __str__(self): 
        return self._nome

  