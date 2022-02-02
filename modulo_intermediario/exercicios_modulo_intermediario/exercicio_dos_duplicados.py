"""
-> É uma lista de listas de números inteiros
-> As listas internas tem o tamanho de 10 elementos
-> As listas internas contém números entre 1 a 10 e eles podem ser duplicados
Exercício
-> Crie uma função que encontra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
        Requisitos:
            A ordem do número duplicado é considerada a partir da segunda
            ocorrência do número, ou seja, o número duplicado em si.
            Exemplo:
                [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
                [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
            Se não encontrar duplicados na lista, retorne -1
"""
lista_professor = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

# print('Neste programa, vamos procurar em uma lista se há numeros repetidos, lista por lista. Se sim vou informar')
# print()
# print('Segue nossa lista abaixo')
# print()
# for imprime in lista_professor:
#     print(imprime)
# print()

# for numero in lista_professor:
#     repetido = []
#     for valor in numero:
#         if valor in repetido:
#             print(f'Na lista {numero}\nO valor {valor} está repetido')
#             print()
#             break
#         else:
#             repetido.append(valor)
#
#     if len(repetido) == len(numero):
#         valor = -1
#         print(f'Na lista {numero}\nnão há números repetidos então retorno {valor}')
#         print()


def checar_duplicados(arg_lista):
    repetido = []
    for valor in arg_lista:
        if valor in repetido:
            return valor
        else:
            repetido.append(valor)

    if len(repetido) == len(arg_lista):
        return -1


for lista in lista_professor:
    print(checar_duplicados(lista))

print(checar_duplicados([1, 2, 3, 4, 5, 6, 7]))
