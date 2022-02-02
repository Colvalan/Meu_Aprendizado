"""
Problema dos parâmetros mutáveis em funções
"""

# Objetos mutáveis = Listas, Dicionários...(coisas que podem ser alteradas)
# Objetos imutáveis = Tuplas, strings, números, True, False, None...(coisas que não podem ser alteradas)


def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['João', 'Maria', 'Eduardo'], ['Kilder'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])
clientes3 = lista_de_clientes(['José'])

print(clientes1)
print(clientes2)
print(clientes3)


