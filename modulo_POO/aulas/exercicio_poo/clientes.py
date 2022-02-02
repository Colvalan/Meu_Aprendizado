from modulo_POO.aulas.exercicio_poo.contas import ContaCorrente, ContaPoupanca


class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def contacorrente(self, agencia, conta, saldo):
        self.conta = ContaCorrente(agencia, conta, saldo)

    def contapoupanca(self, agencia, conta, saldo):
        self.conta = ContaPoupanca(agencia, conta, saldo)

