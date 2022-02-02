"""
Dicionários em python
"""

# Criando dicionário
import copy

print('Primeiro dicionário:')
d1 = {'chave1': 'valor1', 'chave2': 'valor2'}
print(d1)

# Dicionário com muitas chaves:

d2 = {
    1: 2,
    2: 3,
    3: 4
}
print('segundo dicionario')
print(d2)

# Adicionar ou alterar chave de um dicionario

print('segundo dicionario modificado. Chave passou a 20, adicionado chave 4 = 5')
d2[1] = 20
d2[4] = 5
print(d2)

# Modificando dicionário com função .update():

d2.update({5: 6})

print('segundo dicionario modificada com update. Adicionado chave 5 = 6')
print(d2)

# Excluindo chave usando del

del d2[5]

print('Segundo dicionario modificado. Chave 5 excluida')
print(d2)

# Função len() para saber quantas chaves temos

print('Usando função len com segundo dicionário "Temos 4 chaves"')
print(len(d2))

# Iterando dicionários com for

clientes = {
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
    'cliente3': {
        'nome': 'Maria',
        'sobrenome': 'Moreira',
    },
}
print('Iterando o dicionário com for')
for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')

# Copiando dicionários

d3 = copy.deepcopy(d2)

print('Dicionário "d2" copiado para "d3" de forma profunda')
print(d3)

# Fazendo type cast de tuplas e listas para dicionário quando estrutura for similar a um dicionário

lista = [
    ['Kilder', 'Colvalan'],
    ['Natalia', 'Kaio'],
    ['Eliana', 'Colvalan']
]

tupla = (
    ('Danilo', 'Colvalan'),
    ('Edson', 'Colvalan'),
    ('Romildo', 'Braga')
)

print('Printando a lista e checando seu tipo')
print(lista, type(lista))
print('Printando a tupla e checando seu tipo')
print(tupla, type(tupla))

# Agora vamos transformar ambos em dicionários

d4 = dict(lista)
d5 = dict(tupla)

print(d4, type(d4))
print(d5, type(d5))

# Concatenando dicionários

d4.update(d5)

print('Printando d4 com d5 adicionada')
print(d4)
