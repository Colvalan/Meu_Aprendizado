"""
Solit, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list / iteráveis
"""

# A função split neste caso, separar a string em elementos e cria uma lista.
# Com sintaxe string.split('caracter que vai separar a string')
# Nesse exemplo, a lista 1 foi formada separando a string toda vez que houve um espaço entre as palavras.
# A lista 2 foi formada separando a string quando houve ','.

# string = "O Brasil é o pais do futebol, penta campeão mas Brasil está pobre"
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ''
# contagem = 0

# o primeiro for verifica quantas vezes uma palavra apareceu na lista.

# for valor in lista_1:
#     qtd_vezes = lista_1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor

# for valor in lista_2:
#     print(valor.strip().capitalize())  # Função strip tira espaços no fim e no começo do valor. Função capitalize
# # Função Capitalize começa o valor com letra maiúscula.
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')

# Função join, une strings de uma lista em uma unica string.
# A string 1 primeiro foi dividida em uma lista que é a lista 3, depois, uni os elementos da lista de volta
# em uma string que é a string 2. Com sintaxe 'caracter que vai unir os valores'.join(fonte)

# string_1 = 'O Brasil é penta'
# lista_3 = string_1.split(' ')
# string_2 = ' '.join(lista_3)
#
# print(string_1)
# print(lista_3)
# print(string_2)

# Função enumerate desempacota e conta os elementos de uma lista

# Vou criar uma lista que contém outras 3 listas e vou enumeradas com laço for

# lista = [
#     [1, 2],
#     [3, 4],
#     [5, 6],
# ]
#
# for indice, valor in enumerate(lista):
#     print(indice, valor)

# Indice será o valor que retorna de enumerate, e valor será a lista apos o indice.
