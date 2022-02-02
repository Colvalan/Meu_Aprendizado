def listar(lista_atual):
    print(lista_atual)


def adicionar(tarefa):
    lista_atual.append(tarefa)
    lista_secundaria.append(tarefa)


def desfazer(tarefa):
    if not lista_atual:
        print('Não há o que desfazer')
    else:
        lista_atual.pop()


def refazer(tarefa):
    try:
        lista_atual.append(lista_secundaria[len(lista_atual)])
    except IndexError:
        print('Não há o que refazer')


lista_atual = []
lista_secundaria = []

while True:

    tarefa = input('Digite tarefa, ou digite refazer, desfazer ou listar: ')
    if tarefa == 'listar':
        listar(lista_atual)

    elif tarefa == 'refazer':
        refazer(tarefa)

    elif tarefa == 'desfazer':
        desfazer(tarefa)

    else:
        adicionar(tarefa)
