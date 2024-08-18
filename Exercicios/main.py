'''
 07° Lista de exercícios:

        1- Crie uma Classe Pai (Veiculo): Implemente uma classe chamada Veiculo com um construtor que aceita dois parâmetros, 
        marca e modelo. A classe deve ter um atributo protegido _ligado inicializado como False por padrão.
        2- Construa o Método Especial str: Adicione um método especial str à classe Veiculo que retorna uma mensagem formatada 
        com a marca, modelo e o estado de ligado/desligado do veículo.
        3- Crie uma Classe Filha (Carro): Agora, crie uma classe chamada Carro que herda da classe Veiculo. No construtor da classe
        Carro, inclua um novo atributo chamado portas que indica a quantidade de portas do carro.
        4- Implemente o Método Especial str na Classe Filha: Adicione um método especial str à classe Carro que estenda o método da 
        classe pai (Veiculo) e inclua a informação sobre a quantidade de portas do carro.
        5- Crie uma Classe Filha (Moto): Similarmente, crie uma classe chamada Moto que também herda de Veiculo. Adicione um novo atributo 
        chamado tipo ao construtor, indicando se a moto é esportiva ou casual.
        6- Implemente o Método Especial str na Classe Filha (Moto): Adicione um método especial str à classe Moto que estenda o método da 
        classe pai (Veiculo) e inclua a informação sobre o tipo da moto.
        7- Crie um Arquivo Main (main.py): Crie um arquivo chamado main.py no mesmo diretório que suas classes.
        8- Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto 
        com diferentes marcas, modelos, quantidade de portas e tipos.
        9- Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
'''
from projeto.exercicios.carro import Carro
from projeto.exercicios.moto import Moto

carro_1 = {'Fiat', 'Uno - 2013', 3, 'Branco'}
carro_2 = {'Honda', 'Creta - 2018', 5,'Caramelo'}
carro_3 = {'AUDI', 'Q8 - 2024', 5,'Preta'}

moto_1 = {'Shineray', 'SHI-175', 'Esportiva'}
moto_2 = {'Yamaha', 'SCB 300F Twister', 'Casual'}
moto_3 = {'Honda', 'Honda Biz', 'Casual'}

print(carro_1)
print(carro_2)
print(carro_3)

print(moto_1)
print(moto_2)
print(moto_3)