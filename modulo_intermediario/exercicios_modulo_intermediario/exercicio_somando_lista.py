"""

Primeira resolução:

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]

l3 = zip(l1, l2)
l4 = []

for valor in l3:
    valor = sum(valor)
    l4.append(valor)

print(l4)
"""

l1 = [1, 2, 3, 4, 5, 6, 7]
l2 = [1, 2, 3, 4]
l3 = [x[0] + x[1] for x in zip(l1, l2)]
print(l3)
