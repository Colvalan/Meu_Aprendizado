"""
Métodos de Classe.
"""
from random import randint


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):  # Esse é um método de instância. (self)
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):  # Esse é um método de classe (cls)
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod  # Esse é um método estático, não precisasa (nem pode) receber classe ou instancia.
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa.por_ano_nascimento('Kilder', 1992)
print(p1.nome, p1.idade)
print(p1.gera_id())

# Basicamente, neste exemplo, criamos uma pessoa cujo sua idade foi dada a partir de um ano de nascimento
# definido no molde, ou seja, na classe. O que determinou sua criação foi a função por_ano_nascimento que
# que é um método que se referer a classe em si, e não a uma instancia existente.
