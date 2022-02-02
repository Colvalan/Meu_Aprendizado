"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefas
    opção de desfazer (a cada vez que chamarmos, desfaz a última ação)
    opção de refazer (a cada vez que chamarmos, refaz a última ação)
    ['Tarefa 1', 'Tarefa 2']
    ['Tarefa 1'] <- Desfazer
    ['Tarefa 1', 'Tarefa 2'] <- Refazer
    input <- Nova tarefa
"""


def mostrar_op(fazer_lista):
    print()
    print('Tarefas: ')
    print(fazer_lista)
    print()


def desfazer(fazer_lista, refazer_lista):
    if not fazer_lista:
        print('Nada a desfazer')
        return

    ultimo_fazer = fazer_lista.pop()
    refazer_lista.append(ultimo_fazer)


def refazer(fazer_lista, refazer_lista):
    if not refazer_lista:
        print('Nada a refazer')
        return

    ultimo_refazer = refazer_lista.pop()
    fazer_lista.append(ultimo_refazer)


def adicionar(fazer, fazer_lista):
    fazer_lista.append(fazer)


if __name__ == '__main__':
    fazer_lista = []
    refazer_lista = []

    while True:
        fazer = input('Digite uma tarefa ou desfazer, refazer, ls: ')

        if fazer == 'ls':
            mostrar_op(fazer_lista)
            continue
        elif fazer == 'desfazer':
            desfazer(fazer_lista, refazer_lista)
            continue
        elif fazer == 'refazer':
            refazer(fazer_lista, refazer_lista)
            continue

        adicionar(fazer, fazer_lista)
