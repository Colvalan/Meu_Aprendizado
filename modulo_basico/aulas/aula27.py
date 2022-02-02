"""
Desenpacotamento de listas e python
"""
lista = ['Kilder', 'Natalia', 'Eliana', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n1, n2, n3, *resto = lista

print(n1, n2, n3)

# Bem simples, com a sintaxe var = lista, você desempacota o valor. Se houver muitos valores e você precisar
# dos 2 primeiros apenas, pode escrever n1, n2, *restp = lista. Isso faz com que desempacote os 2 primeiros
# valores e coloque o restante em uma outra lista, no caso do exemplo, na lista chamada "resto"

# Alternativamente, se precisar dos ultimos valores, pode digitar *resto, n1, n2, n3 = lista
# Dessa maneira, você desempacota os 3 ultimos valores da lista, e coloca o restante na lista chamado "resto"

