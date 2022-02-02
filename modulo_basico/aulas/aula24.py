"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

# Primeiro vou documentar exemplos de fatiamento de lista

# Quando se fala em fatiamento de listas o conceito é igual ao do fatiamento de strings
# Com sintaxe lista[inicio:fim -1:salto]. Se não especificados, o padrão é 0 para inicio, o fim da lista em fim
# e 1 para salto

#     0  1  2  3  4
l1 = [1, 2, 3, 4, 5]

print(l1[1:])
# Nesse caso, especifiquei o começo apenas, então retornou [2, 3, 4, 5]

l2 = [1, 2, 3, 4, 5]

print(l2[:4])
# Nesse caso, especifiquei o final em 4, então retornou [1, 2, 3, 4]

l3 = [1, 2, 3, 4, 5]

print(l3[::2])
# Nesse caso, especifiquei apenas o salto, então retornou [1,3,5]

# Append, adiciona um valor na lista em seu último indice.

l4 = [1, 2, 3, 4, 5]
l4.append('teste')

print(l4)
# Nesse caso, adicionei a string 'teste' no indice 5 da lista e vai retornar [1, 2, 3, 4, 5, 'teste']

# Insert, adiciona um valor a um indice especifico de uma lista. Com sintaxe .insert(indice, valor)

l5 = [1, 2, 3, 4, 5]
l5.insert(3, 'teste')

print(l5)
# Nesse caso, inseri no indice 3 o valor 'teste' e retornará [1, 2, 3, 'teste', 4, 5]

# O comando pop, exclui o ultimo valor de uma lista.

l6 = [1, 2, 3, 4, 5]
l6.pop()

print(l6)
# Nesse caso, exclui o valor 5 já que ele é o ultimo da lista e retornará [1, 2, 3, 4]

# O comando del de sintaxe del var[indice] exclui um valor específico da lista.

l7 = [1, 2, 3, 4, 5]
del l7[2]

print(l7)

# Nesse caso exclui o indice 2 da lista e retornará [1, 2, 4, 5]

# Também é possível excluir uma faixa de indices com sintaxe entrer colchetes [inicio:fim:salto]

l7 = [1, 2, 3, 4, 5]
del l7[1:3]

print(l7)

# Nesse caso eu exclui a faixa de indices do 1 ao 3, então excluiu os indices 1 e 2, retornando [1, 4, 5]

# Agora vou excluir os indices começando do 0 ao final, pulando de 2 em 2.

l7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del l7[::2]

print(l7)
# Como anunciei, exclui indices de 2 em 2 do começo ao fim, e retornou [2, 4, 6, 8, 10}

# O comando clear, limpa a lista, com sintaxe var.clear()

l8 = [1, 2, 3, 4, 5]
l8.clear()

print(l8)
# Criei uma lista que vai de 1 a 5 porém limpei a mesma com comando clear, e retonará um vazio.

# O comando extend adiciona elementos especificados com sintaxe var.extend([valores])

l9 = [1, 2, 3]
l9.extend([4, 5, 6])

print(l9)
# Aqui eu extendi a lista l9 os valores 4, 5 e 6 e retornará [1, 2, 3, 4, 5, 6]

# Também é possível extender outra lista em uma lista existente com sintaxe var.extend(outra_var)

l9 = [1, 2, 3]
l10 = [4, 5, 6]
l9.extend(l10)

print(l9)
# Extendi a lista l9 com os valores da lista l10 e retornou [1, 2, 3, 4, 5, 6}

# O operador + (soma) concatena listas.

l11 = [1, 2, 3]
l12 = [4, 5, 6]
l13 = l11 + l12

print(l13)
# Agora eu concatenei a lista 11 com a lista 12 e retornou [1, 2, 3, 4, 5, 6]

# Min e Max mostram o menor e maior indice de uma lista com sintaxe min(var) e max(var)

l14 = [1, 2, 3, 4, 5]

print(max(l14), min(l14))
# Aqui pedi pra que seja mostrado o maximo de l14 e o minimo de l14 que retornará 5 1

# O comando range cria listas em um alcance de indices especificado pelo usuário com inicio 0 até onde precisar
# com sintaxe var = list(range(inicio, fim))

l15 = list(range(0, 5))

print(l15)
# Aqui criei uma lista que terá 5 indices, contando do 0 até 4, e retornara [0, 1, 2, 3, 4]
