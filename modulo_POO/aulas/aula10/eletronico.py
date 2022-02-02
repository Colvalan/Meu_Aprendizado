from log import LogMixin


class Eletronico(LogMixin):
    def __init__(self, nome):
        self._nome = nome
        self.ligado = False

    def ligar(self):
        if self.ligado:
            error = f'{self._nome} já está ligado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi ligado corretamente'
        print(info)
        self.log_info(info)
        self.ligado = True

    def desligar(self):
        if not self.ligado:
            error = f'{self._nome} já está desligado'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} foi desligado'
        print(info)
        self.log_info(info)
        self.ligado = False
