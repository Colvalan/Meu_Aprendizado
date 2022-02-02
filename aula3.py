"""
Funções (def) em python - *args **kwargs
Parte 3
"""

# Args: Serve quando não sabemos quantos argumentos colocar na função. Serve parar empacotamente e desempacotamento.


# def func(*args):
#     print(args)
#
#
# lista = [1, 2, 3, 4, 5]
# n1, n2, *n = lista
# print(n1, n2, n)

# Neste caso estou desempacotando os valores da lista sendo n1 = 1, n2 = 2, e n = [3, 4, 5] (restante da lista)

# Agora vou copiar o exemplo do professor explicando que *args é uma tupla empacotada.

# def func (*args):  # Se tornam uma tupla
#     print(args)  # Tupla impressa empacotada
#     print(args[0])  # Acessando o primeiro valor da tupla
#     print(args[-1])  # Acessando o ultimo valor da tupla
#     print(len(args))  # Imprimindo o comprimento da tupla
#
#
# func(1, 2, 3, 4, 5)  # Valores para a função

# É possivel fazer cast de uma tupla para lista com sintaxe args = list(args).

# Exemplo de iteração dentro da função


# def func(*args):
#     for v in args:
#         print(v)
#
#
# func(1, 2, 3, 4, 5)

# kwargs são para argumentos nomeados e diiferentemente dos args, kwargs acompanham 2 "*"

# def func(**kwargs):
#     print(kwargs['nome'], kwargs['sobrenome'])
#
#
# func(nome='kilder', sobrenome='colvalan')

# .get para verificar se argumento existe.


def func(**kwargs):

    nome = kwargs.get('nome')

    if nome is not None:
        print(nome)
    else:
        print('Nome inexistente')


func(nome='Kilder')
