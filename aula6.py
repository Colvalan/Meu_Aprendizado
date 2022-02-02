"""
Tuplas em plython
"""

"""
Tuplas são como listas, porém não podem ser editadas. Muitas das funções que podemos usar em listas, podemos
usar também em tuplas.
Para criar uma tupla, use parenteses, ou apenas separe os elementos com virgula que o python ja entende como tupla.
"""

# Criando tuplas de diferentes maneiras

tupla = (1, 2, 3, 4, 5)
tupla_sem_parenteses = 6, 7, 8, 9, 10
tupla_valor_unico_sem_parenteses = 11,

print(tupla, type(tupla))
print(tupla_sem_parenteses, type(tupla_sem_parenteses))
print(tupla_valor_unico_sem_parenteses, type(tupla_valor_unico_sem_parenteses))
print()

# Acessando indices especificos das tuplas assim como em listas

print(tupla[0])
print(tupla_sem_parenteses[-1])
print()

# Fatiando tuplas assim como em listas

print(tupla[1:])
print()

# Concatenando tuplas assim como em listas

tupla_concatenada = tupla + tupla_sem_parenteses

print(tupla_concatenada)
print()

# Fazendo type cast com tuplas para listas

tupla = list(tupla)

print(tupla, type(tupla))
print()

# Tornando a tupla uma tupla novamente

tupla = tuple(tupla)

print(tupla, type(tupla))

