from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, int):
            raise ValueError('Valor do saldo precisa ser um número')

        self._saldo = valor

    @abstractmethod
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        self._saldo += valor
        print(f'Depósito de R${valor} efetuado com sucesso, seu saldo atual é de R${self.saldo}.')
        self.detalhes()

    def detalhes(self):
        print(f'Agencia : {self.agencia}\n'
              f'Conta : {self.conta}\n'
              f'Saldo : {self.saldo}\n')


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if self.saldo + self.limite < valor:
            print(f'Você não possui fundos suficientes para sacar R${valor}')
            self.detalhes()
            return

        self.saldo = self.saldo - valor
        print(f'Saque efetuado, seu saldo agora é de R${self.saldo}')
        self.detalhes()


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if self.saldo < valor:
            print(f'Você não possui fundos suficientes para sacar R${valor}')
            self.detalhes()
        else:
            self.saldo -= valor
            print(f'Saque efetuado, seu saldo agora é de R${self.saldo}')
            self.detalhes()
