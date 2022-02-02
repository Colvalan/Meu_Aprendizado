from dados import produtos, pessoas, lista
from functools import reduce

# Acumulador convencional

# acumulador = 0
#
# for ac in lista:
#     acumulador += ac
#
# print(acumulador)

# Acumulador com função reduce()

acumulador = reduce(lambda ac, x: x + ac, lista, 0)
                        # ac é onde os numeros vão ser acumulados
                        # x serão os valores da lista em cada iteração do laço
                        # x + ac é a formula aplicada a cada iteração
                        # lista, é o iterável que será iterado
                        # 0 é o valor que "ac" terá no primeiro laço
print(acumulador)

# Somar os preços dos produtos usando reduce()

precos_somados = reduce(lambda soma, x: x['preco'] + soma, produtos, 0)
print(precos_somados)

# Somar e pegar a média de idade da lista "pessoas"

idades_somadas = reduce(lambda soma, x: x['idade'] + soma, pessoas, 0)
print(idades_somadas / len(pessoas))

# Exemplo do caderno

produtos1 = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p2', 'preco': 55},
    {'nome': 'p3', 'preco': 5},
]


precos_somados1 = reduce(lambda soma, x: x['preco'] + soma, produtos1, 0)
print(precos_somados1)


# Exemplo do caderno 2

pessoas1 = [
    {'nome': 'Kilder', 'idade': 29},
    {'nome': 'Natalia', 'idade': 30},
    {'nome': 'Danilo', 'idade': 34},
]

idades_somadas1 = reduce(lambda soma, x: x['idade'] + soma, pessoas1, 0)
print(idades_somadas1 / len(pessoas1))
