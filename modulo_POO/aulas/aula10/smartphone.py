from eletronico import Eletronico
from log import LogMixin


class Smartphone(Eletronico, LogMixin):  #Herda primeiro de Eletronico depois de Logmixin
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self.ligado:
            erro = f'{self._nome} não está ligado'
            print(erro)
            self.log_error(erro)
            return

        if self._conectado:
            erro = f'{self._nome} JÁ ESTÁ CONECTADO'
            print(erro)
            self.log_error(erro)
            return

        info = f'O {self._nome} está conectado'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            erro = f'{self._nome} NÃO ESTÁ CONECTADO'
            print(erro)
            self.log_error(erro)
            return

        info = f'O {self._nome} foi desligado'
        print(info)
        self.log_info(info)
        self._conectado = False
