"""
Count - Itertools
"""

# Exemplo de contador

from itertools import count

contador = count()

for valor in contador:
    print(valor)
    if valor >= 10:
        break

contador_reverso = count(step=-1)
print()
print('Contador Reverso')
print()

for valor in contador_reverso:
    print(valor)
    if valor <= -10:
        break

contador_2_em_2 = count(step=2)
print()
print('Contador de 2 em 2')
print()

for valor in contador_2_em_2:
    print(valor)
    if valor >= 10:
        break

contador_reverso = count(start=5)
print()
print('Contador a partir de 5')
print()

for valor in contador_reverso:
    print(valor)
    if valor >= 10:
        break

contador_float = count(step=0.1)
print()
print('Contador como float de 0.5')
print()

for valor in contador_float:
    print(round(valor))
    if valor >= 10:
        break