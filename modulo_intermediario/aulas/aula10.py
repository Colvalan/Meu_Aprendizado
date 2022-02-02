"""
List comprehension em python
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]
print('Copiei a lista usando um for')
print(ex1)
print()

ex2 = [v * 2 for v in l1]
print('Multipliquei os elementos da lista por 2 usando for')
print(ex2)
print()

ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print('Adicionei coordenadas ,0 ,1 e ,2 em casa elemento da lista usando for e range(3)')
print(ex3)
print()

l2 = ['luiz', 'Mauro', 'Maria']
ex4 = [v.replace('a', '@').upper() for v in l2]
print('Formatei a lista ["Luiz", "Mauro", "Maria"] em caixa alta e substitui os "a" por "@" usando replace e .upper')
print(ex4)
print()

tupla = (('chave', 'valor'), ('chave2', 'valor2'))
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)
print('Inverti os valores com as chaves da tupla criada, e as transformei em dicionário')
print('Era = (("chave", "valor"), ("chave2", "valor2"))')
print(f'Agora = {ex5}')
print()

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0]
print('Criei uma lista de 0 a 99 usando "list(range(100))" e vou mostrar apenas divisíveis por 3')
print('Usando for e if na criação desta lista com os divisíveis')
print(ex6)
print()

ex7 = [v if v % 3 == 0 else 0 for v in l3]
print('Agora vamos mostrar apenas divisíveis por 3, e o que não for, passará a ser 0')
print('Para isso usei if, else e depois for')
print(ex7)
print()

lista_sem_0 = []

for valor in ex7:
    if valor == 0:
        pass
    else:
        lista_sem_0.append(valor)

print(lista_sem_0)
