"""
Geradores. iteradores e iteráveis\
"""

# convertendo um iterável (lista) em iterador.

# lista = [1, 2, 3, 4, 5]
# lista = iter(lista)
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))


# def gerador():
#     for n in range(100):
#         yield n
#         time.sleep(1)
#
#
# g = gerador()
#
# for i in g:
#     print(i)

# Exemplo de gerador mais simples de criar.

# lista = [x for x in range(1000)]  # Lista de 0 a 999
# lista2 = (x for x in range(1000))  # Gerador de 0 a 999
#
# print(f'Percebe-se que o tipo da lista é', type(lista))
# print(f'Percebe-se que o tipo da lista2 é', type(lista2))

# Comportamento dos iteradores e geradores

# '''
# Iteradores tem um valor finito, numa string de 6 caracteres como 'Kilder', o iterador poderá ser usado
# 6 vezes, uma 7° vez, traria uma excecão 'Stop Iteration'. Se eu printar esse iterador 3 vezes, e fizer um for
# esse for só vai me trazer mais 3 iterações, e encerrará automaticamente, veja abaixo:
# '''
#
# str = 'kilder'
# str = iter(str)
#
# print(next(str))  # k
# print(next(str))  # i
# print(next(str))  # l
# print('---------------------')
# print('for continua')
#
# for letra in str:
#     print(letra)
#
# print('iterador "str" se esgota.')

lista = [1, 2, 3, 4, 5]
lista2 = [x * 2 for x in lista]
print(lista2)