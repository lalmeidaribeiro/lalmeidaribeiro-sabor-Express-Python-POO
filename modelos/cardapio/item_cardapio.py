from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod #Todas as classes derivadas dessa, precisam ter o desconto, do contrario o codigo vai parar
    def aplicar_desconto(self):
        pass
          