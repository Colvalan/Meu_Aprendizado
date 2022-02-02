"""
Faça uma lista de tarefas com as seguintes opções:
    adicionar tarefa
    listar tarefa
    opção de desfazer (a cada vez que chamarmos, desfaz a ultima ação)
    opção de refazer (a cada vez que chamarmos, refaz a ultima ação)
"""

# O programa começa com bloco try porque no início, pode haver arquivo tarefas.txt já existente de outras execuções.
# Primeiro, abri o arquivo e fiz leitura
# Depois, criei uma var chamada string e coloquei o conteúdo do arquivo nesta var usando .read().
# Transformo a string em uma lista chamada "tarefas" usando .split()
# Por fim, excluo o ultimo valor da lista que na verdade é uma quebra de linha adicionada pelo programa.
# Caso não haja arquivo existente, crio uma lista chamada "tarefas" nova em branco.
# Posteriormente, a lista "tarefas" terá todo seu conteúdo gravado em novo arquivo de texto chamado "tarefas.txt".

try:
    arquivo = open('tarefas.txt', 'r')
    string = arquivo.read()
    tarefas = string.split('\n')
    tarefas.pop()
except:
    tarefas = []

# Criei uma variável chamada ultima_tarefa para armazenar a última tarefa digitada pelo usuário.
# Seu valor inicial é None.

ultima_tarefa = None

# Criei uma variável chamada tarefa que será alimentada pelo usuário. Seu valor inicial também é None.

tarefa = None

# Usei while para que o programa só pare se o usuário quiser.

while True:

    # Variável "comando", que é alimentada pelo usuário, define os próximos passos do programa.

    comando = input('Lista de comandos:\n\nA = Adicionar tarefa\nL = Listar suas tarefas\n'
                    'D = Desfazer ação\nR = Refazer ação\nS = Sair do programa e salvar dados\n'
                    '\nO que deseja fazer?: ')
    print()

    # Se o comando for 'A' de "Adicionar tarefa", o programa solicita que o usuário descreva a tarefa.
    # Após isso, adiciona essa tarefa à lista "tarefas".
    # Ainda defino a ultima_tarefa como a tarefa que foi digitada.
    # Por fim, mostro ao cliente que sua tarefa foi adicionada com sucesso na lista.

    if comando == 'A':
        tarefa = input('Digite uma tarefa a ser adicionada: ')
        tarefas.append(tarefa)
        ultima_tarefa = tarefa
        print(f'A tarefa {tarefa} foi adicionada com sucesso.')

    # Se o comando for 'L' de "Listar suas tarefas", faço uma iteração sobre a lista atual.
    # E mostro as tarefas listadas atualmente.

    if comando == 'L':
        if not tarefas:
            print('Não há tarefas a serem listadas.')
            print()
            continue
        print('Segue a lista com suas tarefas:')
        print()
        for i in tarefas:
            print('◉ ', i)
        print()

    # Se o comando for 'D' de "Desfazer ação", primeiro verifico se realmente há uma ação a ser desfeita.
    # Se não há ação a ser desfeita, comunico isso ao usuário e reinicio o loop.
    # Se há ação a ser desfeita, excluo a ultima tarefa que foi adicionada na lista e comunico isso ao usuário.

    if comando == 'D':
        if tarefa is None:
            print('Não existe ação a ser desfeita.')
            continue
        print(f'A tarefa {tarefas[-1]} foi removida')
        tarefas.pop()
        print()

    # Se o comando for 'R' de "Refazer ação", primeiro verifico de realmente há ação a ser refeita.
    # Se não há ação a ser refeita, comunico ao usuário e reinicio o loop.
    # Se há ação a ser refeita, adiciono novamente à lista a ultima tarefa adicionada e comunico isso ao usuário.

    if comando == 'R':
        if tarefa is None:
            print('Não existe ação a ser refeita.')
            continue
        tarefa = tarefas.append(ultima_tarefa)
        print(f'A tarefa {ultima_tarefa} foi adicionada')
        print()

    # Se o comando for 'S' de "Sair do programa e salvar dados", mostro a lista atual.
    # Faço uma checagem extra se o usuário deseja realmente sair e regravar os dados. Se sim encerro o loop.
    # Se não, recomeço o loop.

    if comando == 'S':
        print('Assim ficou a sua lista de tarefas:')
        print()
        for i in tarefas:
            print('◉ ', i)
        print()
        checagem_saida = input('Deseja mesmo sair e gravar estes dados?\n'
                               'Dados anteriores serão perdidos!\n'
                               '[S] = Sim\n'
                               '[N] = Não: ')
        if checagem_saida == 'S':
            print('Programa encerrado.')
            break
        elif checagem_saida == 'N':
            continue

# Por fim, gravo os dados da lista em arquivo de texto e aviso isso ao usuário.

file = open('tarefas.txt', 'w+')

for valor in tarefas:
    file.write(f'{valor}\n')

print()
print('Dados foram salvos em "tarefas.txt".')

# Fim do programa.
