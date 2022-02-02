from time import sleep
from threading import Thread, Lock


"""
class MeuThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo
        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MeuThread('Thread 1', 5)
t1.start()

t2 = MeuThread('Thread 2', 3)
t2.start()

t3 = MeuThread('Thread 3', 1)
t3.start()

for i in range(10):
    print(i)
    sleep(1)
"""
"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Thread 1', 5))
t1.start()

t2 = Thread(target=vai_demorar, args=('Thread 2', 3))
t2.start()

t3 = Thread(target=vai_demorar, args=('Thread 3', 1))
t3.start()

for i in range(10):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Thread 1 foi executada', 10))
t1.start()

while t1.is_alive():
    print('Aguardando Thread 1 ser executada')
    sleep(3)

print('Fim do código')
"""


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()  # O lock, é o que vai trancar as threads uma por uma.

    def comprar(self, quantidade):
        self.lock.acquire()  # Aqui, quando a thread entra nesse método, o lock tranca.

        if self.estoque < quantidade:
            print('Não temos ingressos suficientes.')
            self.lock.release()  # Se estoque for menor que quantidade, o lock libera a thread.
            return

        sleep(1)

        # SE NÃO...

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingressos. Ainda temos {self.estoque} ingressos.')
        self.lock.release()  # Libera a thread depois de tudo feito, e libera a próxima entrada.


if __name__ == '__main__':
    ingressos = Ingressos(50)

    threads = []  # Lista vazia que vai receber as threads conforme o for abaixo.
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        threads.append(t)  # Cada laço, uma thread criada vai para lista de threads.

    for t in threads:
        t.start()  # Aqui, todas as threads contidas na lista, serão iniciadas.

    executando = True  # Verificador para o while.

    while executando:
        executando = False  # Seta o valor para False. Só voltará a ser True caso há uma thread viva.

        for t in threads:  # Vai verificar na lista, thread a thread, se há threads vivas.
            if t.is_alive():
                executando = True  # Se sim, seta o valor para True, while reiniciará até que todas as threads terminem.
                break

    print(f'Restaram {ingressos.estoque} ingresso(s)')  # Terminando, mostra quantos ingressos restaram.
