'''
    07° Lista de exercícios:

        1- Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, 
        marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
        2- Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada 
        com a marca, modelo e o estado de ligado/desligado do veículo.
        3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe
        Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
'''
class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo 
        self._ligado  = False

    def __str__(self):
        status = "ligado" if self._ligado else "desligado"
        return f"Marca: {self.marca} | Modelo: {self.modelo} |  Status: {status}"

    