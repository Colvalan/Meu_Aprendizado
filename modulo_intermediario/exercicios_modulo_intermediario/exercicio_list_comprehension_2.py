"""
Neste exercicio, devemos somar o valor das tuplas usando list comprehension
"""

carrinho = [('Produto 1', 30.5), ('Produto 2', 20), ('Produto 3', 50)]

total = sum([float(y[1]) for y in carrinho])
print(total)

"""
Compreendi o exercicio, só não estava conseguindo somar os valores na mesma linha.
Ai o professor usou o comando 'sum()' e colocou como parametro toda a formação da lista
Com isso, ele pode somar os resultados.

Eu estava somando depois de criar a lista, ou seja, na linha 8, eu estava colocando total = sum(total) e depois
printando. Não considerei que fiz 100% o exercicio pq o professor pediu que isso fosse feito em duas linhas
e nesse caso usei 2 linhas.
"""