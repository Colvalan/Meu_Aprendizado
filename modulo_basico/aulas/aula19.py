"""
While em Python

Utilizado para realizar ações enquanto uma condição for verdadeira.

Requisitos: Entender condições e operadores.
"""

# exemplo de loop infinito:

"""
while True:
    nome = input('Qual é o seu nome? ')
    print(f'Olá {nome}!')

print('Isso nunca será impresso na tela')  #já que a condição deste while é sempre True.
"""

# contador até 5.

"""
x = 0

while x < 5:
    print(x)
    x = x + 1

print('Fim da contagem. Vamos de novo!')
"""

# Exemplo da função "continue" - Essa função faz com que o não seja executado linhas posteriores ao "continue"
# reiniciando o laço do while.

"""
x = 0

while x < 10:

    if x == 3:  # Se x == 3, some + 1 em X apenas e continue sem printar a variável.
        x = x + 1
        continue

    print(x)
    x = x + 1

print('Acabou a contagem e pulei o 3')
"""

# Função break - a função break encerra o laço.

"""
x = 0

while x < 10:

    if x == 3:
        x = x + 1
        break

    print(x)
    x = x + 1

print('Só contei ate 2 porque quando X fosse igual a 3 você mandou parar o laço com break!')
"""

# Agora, exemplo de while dentro de while

"""
x = 0

while x <= 10:
    y = 0

    while y <= 5:
        print(f'{x},{y}')
        y = y + 1

    x = x + 1

print('fim!')
"""

# Calculadora simples usando while.

while True:
    print()
    num_1 = input('Digite o primeiro número: ')
    num_2 = input('Digite o segundo número: ')
    operador = (input('Escolha um operador: Soma [+] Substração [-]  Divisão [/] Multiplicação [*]: '))

    if num_1.isalpha() or num_2.isalpha():
        print('Amigo, você precisa digitar um número né?')
        sair = input('Alternativamente, se você for burro pode quitar a calculadora. deseja sair? [s]im ou [n]ao?')

        if sair == 's':
            break
        else:
            continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)

    elif operador == '-':
        print(num_1 - num_2)

    elif operador == '*':
        print(num_1 * num_2)

    elif operador == '/':
        print(num_1 / num_2)

    else:
        print('Amigo, digite um operador válido conforme mostrado na tela né? Me ajuda ai.')
