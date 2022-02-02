"""
Combination, Permutations e Product - Itertools
Combinação = Ordem não importa
Permutação = Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

lista = ['Kilder', 'Xito', 'Zé', 'Danilo']

print()
print('Product')
print()

for combinacao in product(lista, repeat=2):
    print(*combinacao, sep=' X ')

print()
print('Combinations')
print()

lista = ['Kilder', 'Xito', 'Zé', 'Danilo']

for combinacao in combinations(lista, 2):
    print(*combinacao, sep=' X ')

print()
print('Permutations')
print()

lista = ['Kilder', 'Xito', 'Zé', 'Danilo']

for combinacao in permutations(lista, 2):
    print(*combinacao, sep=' X ')
