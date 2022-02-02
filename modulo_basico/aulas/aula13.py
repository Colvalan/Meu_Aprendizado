"""
Função len
Serve para contar os caracteres de uma string
"""

# Nesse exemplo eu pedi pro python contar quantos caracteres foi digitado pelo usuário.

"""
usuario = input('Digite o nome do usuário: ')
qt_caracteres = len(usuario)

print(f'O nome de usuário possúi {qt_caracteres} caractéres')
"""

# Nesse exemplo, vou pedir que o usuário digite no mínimo 6 caractéres.

"""
usuario = input('Digite um nome de usuário com pelo menos 6 caractéres: ')
qt_caracteres = len(usuario)

if qt_caracteres < 6:
    print('O nome de usuário precisa ter no mínimo 6 caractéres!')
else:
    print('Você se cadastrou com sucesso!')
"""

# Nesse exemplo irei somar a quantidade de caractéres digitados pelo usuário

palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite uma outra palavra: ')

print(f'A quantidade de caractéres digitados foi de {len(palavra1) + len(palavra2)} caractéres')
