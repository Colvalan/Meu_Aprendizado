"""
Classes - POO
"""
from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return

        if self.falando:
            print(f'{self.nome} não pode comer porque está falando.')
            return

        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

    def falar(self, assunto):
        if self.falando:
            print(f'{self.nome} já está falando.')
            return

        if self.comendo:
            print(f'{self.nome} não pode falar comendo.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} já não estava falando.')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade


p1 = Pessoa('Kilder', 29)
p1.falar('Ronaldo')
p1.comer('pizza')
print(p1.get_ano_nascimento())