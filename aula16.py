from dados import produtos, pessoas, lista


# nova_lista = map(lambda x: x * 2, lista)  # função map para multiplicar os valores da lista original

# Vamos fazer agora um list comprehension que é similar.

# nova_lista = [x * 2 for x in lista]
# print(lista)
# print(list(nova_lista))

# Somando 5% de cada preco constado no iteravel produtos

# def aumenta_preco(p):
#     p['preco'] = round(p['preco'] * 1.05, 2)  # o '2' são as casas decimais a serem mostradas.
#     return p
#
#
# novos_precos = map(aumenta_preco, produtos)
#
#
# for preco in novos_precos:
#     print(preco)

# Adicionando chaves com a mesma logica. Só é necessário alterar a função

def aumenta_preco(p):
    p['preço reajustado'] = round(p['preco'] * 1.05, 2)  # o '2' são as casas decimais a serem mostradas.
    return p


novos_precos = map(aumenta_preco, produtos)

for preco in novos_precos:
    print(preco)
