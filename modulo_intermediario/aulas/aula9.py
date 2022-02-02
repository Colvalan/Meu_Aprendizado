"""
Sets emm Python

add (adiciona), update (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetric_difference ^ (elementos que estão nos dois sets, mas não em ambos)
"""

# Criando o set

s1 = {1, 2, 3}
print('set completo como criado')
print(s1)


# Adicionando elemento

s1.add(4)

print()
print('valor 4 adicionado com .add()')
print(s1)  # Valor 4 adicionado corretamente.

s1.update('python')

print()
print('string python foi adicionado usando .update()')
print(s1)

s1.discard(1)

print()
print('Valor 1 removido com .discard()')
print(s1)

s1.clear()

print()
print('Set limpo com comando .clear()')
print(s1)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = s1 | s2

print()
print('Criei s1 como {1, 2, 3} e s2 como {4, 5, 6} e uni ambas com Union (|) em S3')
print(s3)

s1 = {1, 2, 3}
s2 = {1, 2, 3, 4}
s3 = s1 & s2

print()
print('Criei S1 como {1, 2, 3} e s2 como {1, 2, 3, 4} e vou mostrar apenas o que está em ambas com "&" em S3')
print(s3)

s3 = s2 - s1

print()
print('Agora vou mostrar apenas o que está a mais em S2 usando Difference (-)')
print(s3)

s1 = {1, 2, 4}
s2 = {1, 2, 3}
s3 = s1 ^ s2

print()
print('Agora vou mostrar o que há em s1 e não em s2, e o que há em s2 e não em s1')
print('Para isso criei S1 como {1,2,4} e s2 como {1, 2, 3}')
print(s3)
