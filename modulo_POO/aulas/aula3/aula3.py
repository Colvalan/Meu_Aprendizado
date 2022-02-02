"""
Getters e setters em POO
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))
        return self.preco

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()

    # Getter
    @property
    def preco(self):  # Devemos nomear esse getter com o nome da variavel que ele vai capturar
        return self._preco  # Por convenção, adicionamos _ antes do nome.

    # Setter
    @preco.setter  # O decorador deve ter o nome da variavel que foi capturada pelo Getter, e que será modificada.
    def preco(self, valor):  # Valor vem do getter automaticamente.
        if isinstance(valor, str):  # Checa se é uma string. Se sim é o que segue:
            valor = float(valor.replace('R$', ''))  # Type cast para float, e substitui R$ por vazio
        self._preco = valor  # O valor obtido vai para a _preco que por consequencia também vai para self.preco.


p1 = Produto('CADEIRA', 'R$50')
p1.desconto(10)
print(p1.nome, p1.preco)

"""
O que fizemos aqui foi usar o Getter para capturar o preco, e o setter para configurá-lo de forma
que formatou o R$50, para 50 e o transformou em inteiro. Getters e Setters podem resolver esse tipo de
problema sem mexer no código que já está pronto.
"""