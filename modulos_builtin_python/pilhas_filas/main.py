"""
LIFO, de Last in, First Out, é uma estrutura de dados semelhante á uma pilha de livros.
Conforme empilhamos os livros, a pilha cresce, e quando tiramos um livro, o livro que sai é o ultimo
a ter sido empilhado.

Essa é uma estrutura de dados comum em python que pode ser representada facilmente com uma lista.

pilha = list()  # lista vazia sem nenhum "livro"
pilha.append('Livro 1')
pilha.append('Livro 2')
pilha.append('Livro 3')
pilha.append('Livro 4')
pilha.append('Livro 5')

# Temos agora uma "pilha" de 5 livros.

pilha.pop()  # Tiramos o Livro 5.

Ou seja, o ultimo a entrar, foi o primeiro a sair. De Last in, First Out, ou LIFO!

Agora vamos imaginar uma fila de bando onde o primeiro a sair, é quem foi o primeiro a chegar.
Ai teremos o FIFO, ou First in, First out. É uma estrutura de dados que pode causar efeitos
colaterais em python já que se representadas por uma lista comum, sempre que o primeiro dado sair da lista
todos os outros andaram 1 'casa' para esquerda, e isso mudaria todos os indices. Em uma fila grande
causaria problemas de performance no programa.

Usaremos deque de collections, para este tipo de estrutura:

"""

# from collections import deque
#
# fila = deque()
# fila.append('Joãozinho')
# fila.append('Maria')
# fila.append('Luiz Otavio')  # Possuimos um fila com 5 pessoas. Joãozinho chegou primeiro.
# fila.append('Marcos')
# fila.append('José')
# print(f'Saiu: {fila.popleft()}')  # Joãozinho é o primeiro a sair.
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
# print(f'Saiu: {fila.popleft()}')
#
# # Até que sairam todos!
#
# for nome in fila:
#     print(nome)

from collections import deque

fila = deque(maxlen=5)
fila.extend([1, 2, 3, 4])
fila.append(5)
fila.append(6)

print(fila)