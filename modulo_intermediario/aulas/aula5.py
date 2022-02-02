"""
Expressões Lambda
"""
# São funções que não precisam ser definidas e depois utilizadas no código. Veja exemplo:

# preco = 1000
# preco2 = 2000

# Vou criar uma função que calcula 30% de imposto sobre o preço pré definido.


# def calcular_imposto(arg):
#     return arg * 0.3


# print(calcular_imposto(preco))

# Agora farei uma função lambda que vai funcionar exatamente como a função def mas como o preco2

# calcular_imposto2 = lambda x: x*0.3
#
# print(calcular_imposto2(preco2))

# A função lambda recebeu em 'x' o parâmetro de 'preco2' ou seja, '2000'. Por isso executou 2000 * 0,3

# Ordenando uma lista com lambda.
# Existem duas formas, alterando a lista original, e alterando apenas no print com lambda.
# Primeiro, vamos ordenar a lista original

# lista = [
#     ['P1', 13],  # Item 0 = nome | Item 1 = preço
#     ['P2', 6],  # Item 0 = nome | Item 1 = preço
#     ['P3', 7],  # Item 0 = nome | Item 1 = preço
#     ['P4', 50],  # Item 0 = nome | Item 1 = preço
#     ['P5', 8]  # Item 0 = nome | Item 1 = preço
# ]
#
#
# def func(item):
#     return item[1]  # Essa será a chave ou 'key' para ser usada na hora de ordenar com função sort.
#                     # Ou seja, ordenará pelo indice 1.
#
#
# lista.sort(key=func)  # A função .sort vai funcionar como uma iteração sobre a lista e ordenar usando o indice 1
#                       # de cada lista dentro de 'lista', porque isso foi especificado na função 'func'
# print(lista)

# Se eu quiser inverter a ordem, devo usar reverse=True após o parametro de sort. Ficaria dessa maneira:
# lista.sort(key=func, reverse=True)

# Agora com lambda.

# lista = [
#     ['P1', 13],  # Item 0 = nome | Item 1 = preço
#     ['P2', 6],  # Item 0 = nome | Item 1 = preço
#     ['P3', 7],  # Item 0 = nome | Item 1 = preço
#     ['P4', 50],  # Item 0 = nome | Item 1 = preço
#     ['P5', 8]  # Item 0 = nome | Item 1 = preço
# ]
#
# lista.sort(key=lambda item: item[1])
# print(lista)

# Ambos ultimos exemplos, alteraram a ordem da lista original.
# Agora, vamos manter a lista original intacta, e ordena-la apenas no print.

lista = [
    ['P1', 13],  # Item 0 = nome | Item 1 = preço
    ['P2', 6],  # Item 0 = nome | Item 1 = preço
    ['P3', 7],  # Item 0 = nome | Item 1 = preço
    ['P4', 50],  # Item 0 = nome | Item 1 = preço
    ['P5', 8]  # Item 0 = nome | Item 1 = preço
]

print(sorted(lista, key=lambda i: i[1]))  # Lista ordenada apenas no print
print(lista)  # Lista sem ordenação, com sua estrutura intacta.
