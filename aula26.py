"""
Funções decoradoras e decoradores
"""
from time import time, sleep


def velocidade(funcao):  # Função decoradora que recebe uma função decorada
    def interna(*args, **kwargs):  # Função que vai adicionar uma funcionalidade a função decorada
        start_time = time()  # Tempo de inicio da execução
        resultado = funcao(*args, **kwargs)  # Resultado é igual a função decorada
        end_time = time()  # Tempo do fim da execução
        tempo = (end_time - start_time) * 1000  # Calculo para saber em ms quanto demorou para o codigo ser executado.
        print(f'\nA função {funcao.__name__} '  # Print do resultado
              f'levou {tempo:.2f}ms para executar')
        return velocidade  # Retorna função não executada
    return interna  # Retorna função não executada


@velocidade  # decorador
def demora():  # função que foi decorada
    for i in range(1, 6):
        print(i)
        sleep(0)


demora()
