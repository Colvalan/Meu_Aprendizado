class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclasse} comprando...')

    def falar(self):
        print('Estou em cliente')


class ClienteVIP(Cliente):  # ClienteVIP herda primeiro de Cliente, depois de Pessoa.
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)  # herdou o construtor de Pessoa para atributos nome e idade.
        self.sobrenome = sobrenome  # atributo sobrenome pertence apenas a ClienteVIP

    def falar(self):  # Sobrepondo o método falar da classe Pessoa.
        Pessoa.falar(self)  # Vamos chamar o método de Pessoa
        Cliente.falar(self)  # Vamos chamar o método de Cliente
        print(f'{self.nome} {self.sobrenome}')  # Função própria do método pertencente apenas a ClienteVIP.
