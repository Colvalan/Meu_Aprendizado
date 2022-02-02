class Ip:
    def __init__(self, ip: str, cidr: int):
        self.ip = ip
        self.cidr = cidr
        self.total_hosts = 2 ** (32 - self.cidr) - 2
        self.subrede_decimal = 0
        self.rede = 0
        self.broadcast = 0
        self.ultimo_ip = 0
        self.primeiro_ip = 0

    @property
    def cidr(self):
        return self._cidr

    @cidr.setter
    def cidr(self, valor):
        if valor < 24 or valor > 32:
            raise ValueError('O valor de CIDR deve ser um número entre 24 e 32.')

        self._cidr = valor

    @property
    def subrede_decimal(self):
        return self._subrede_decimal

    @subrede_decimal.setter
    def subrede_decimal(self, valor):
        if self.cidr == 24:
            subrede_oct4 = '0'
        elif self.cidr == 25:
            subrede_oct4 = '128'
        elif self.cidr == 26:
            subrede_oct4 = '192'
        elif self.cidr == 27:
            subrede_oct4 = '224'
        elif self.cidr == 28:
            subrede_oct4 = '240'
        elif self.cidr == 29:
            subrede_oct4 = '248'
        elif self.cidr == 30:
            subrede_oct4 = '252'
        elif self.cidr == 31:
            subrede_oct4 = '254'
        else:
            subrede_oct4 = '255'

        self._subrede_decimal = '255.255.255.' + subrede_oct4

    @property
    def rede(self):
        return self._rede

    @rede.setter
    def rede(self, valor):
        ip = list(self.ip)

        if ip[-2] == '.':
            ip.pop()
            ip.append('0')

        elif ip[-3] == '.':
            ip.pop()
            ip.pop()
            ip.append('0')

        elif ip[-4] == '.':
            ip.pop()
            ip.pop()
            ip.pop()
            ip.append('0')

        self._rede = ''.join(ip)

    @property
    def broadcast(self):
        return self._broadcast

    @broadcast.setter
    def broadcast(self, valor):
        ip = list(self.ip)

        if ip[-2] == '.':
            ip.pop()
            ip.append(str(self.total_hosts + 1))

        elif ip[-3] == '.':
            ip.pop()
            ip.pop()
            ip.append(str(self.total_hosts + 1))

        elif ip[-4] == '.':
            ip.pop()
            ip.pop()
            ip.pop()
            ip.append(str(self.total_hosts + 1))

        self._broadcast = ''.join(ip)

    @property
    def ultimo_ip(self):
        return self._ultimo_ip

    @ultimo_ip.setter
    def ultimo_ip(self, valor):
        ip = list(self.ip)

        if ip[-2] == '.':
            ip.pop()
            ip.append(str(self.total_hosts))

        elif ip[-3] == '.':
            ip.pop()
            ip.pop()
            ip.append(str(self.total_hosts))

        elif ip[-4] == '.':
            ip.pop()
            ip.pop()
            ip.pop()
            ip.append(str(self.total_hosts))

        self._ultimo_ip = ''.join(ip)

    @property
    def primeiro_ip(self):
        return self._primeiro_ip

    @primeiro_ip.setter
    def primeiro_ip(self, valor):
        ip = list(self.ip)

        if ip[-2] == '.':
            ip.pop()
            ip.append('1')

        elif ip[-3] == '.':
            ip.pop()
            ip.pop()
            ip.append('1')

        elif ip[-4] == '.':
            ip.pop()
            ip.pop()
            ip.pop()
            ip.append('1')

        self._primeiro_ip = ''.join(ip)
