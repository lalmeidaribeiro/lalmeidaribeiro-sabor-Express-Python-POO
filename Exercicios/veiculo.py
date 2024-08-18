'''
    07° Lista de exercícios:

        1- Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, 
        marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
        2- Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada 
        com a marca, modelo e o estado de ligado/desligado do veículo.
        3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe
        Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.

        -----------------------------------------------------------------------------------------------------------------------------
    08° Lista de exercícios
        1- Crie uma classe chamada Veiculo com um método abstrato chamado ligar.
        2- No mesmo arquivo, crie um construtor para a classe Veiculo que aceita os parâmetros marca e modelo.
        3- Crie uma nova classe chamada Carro que herda da classe Veiculo.
        4- No construtor da classe Carro, utilize o método super() para chamar o construtor da classe pai e 
        atribua o atributo específico cor à classe filha.
        5- Em um arquivo chamado main.py, importe a classe Carro.
        6- No arquivo main.py, instancie três objetos da classe Carro com diferentes características, 
        como marca, modelo e cor.
        '''
from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo 
        #self._ligado  = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        #return f"Marca: {self.marca} | Modelo: {self.modelo} |  Status: {status}"
        return f'Marca: {self.marca} | Modelo: {self.modelo}'
    
    
    @abstractmethod
    def ligar_veiculo():
        pass

    