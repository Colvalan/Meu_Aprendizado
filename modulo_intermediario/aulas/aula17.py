from dados import produtos, pessoas, lista

# Filtrar lista usando filter()

# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))

# Filtrar lista usando list comprehension

# nova_lista = [x for x in lista if x > 5]
# print(nova_lista)

# Filtrando dicionario com filter

# produtos_filtrados = filter(lambda x: x['preco'] > 50, produtos)
#
# for produtos in produtos_filtrados:
#     print(produtos)

# Para coisas mais complexas, usar função. Lembre-se, filter, retorna True ou False.


# def filtro(produto):
#     if produto['preco'] > 50:
#         return True
#
#
# produtos_filtrados = filter(filtro, produtos)
#
# for produtos in produtos_filtrados:
#     print(produtos)

# Filtrando nomes por maioridade usando filter


def filtro(i):
    if i['idade'] >= 18:
        return True


maiores = filter(filtro, pessoas)

for maior in maiores:
    print(maior)