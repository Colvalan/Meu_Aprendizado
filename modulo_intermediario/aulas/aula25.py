#  Criar ler e escrever arquivos em python
#  Documentação em https://docs.python.org/3/library/functions.html#open

import os
import json

# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
#
# file.seek(0, 0)
# print('Lendo linhas:')
# print(file.read(), end='')
# print('#####################')
#
# file.seek(0, 0)
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print('#####################')
#
# file.seek(0, 0)
#
# print(file.readlines())
# print('#####################')
# file.seek(0, 0)
#
# for linha in file.readlines():
#     print(linha, end='')
#
# file.close()

# Com try não é muito 'pythonico' mas segue exemplo

# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#     file.seek(0, 0)
#     print(file.read())
# finally:
#     file.close()

# Melhor maneira de se trabalhar no python com arquivos é o que segue:

# with open('abc.txt', 'w+') as file:
#     file.write('Linha 1\n')
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#     file.seek(0)
#     print(file.read())

# Dessa maneira, o gerenciador "with" fecha o arquivo automaticamente.

# with open('abc.txt', 'r') as file:  # Usando 'r' fazemos apenas leitura do arquvo
#     print(file.read())

# with open('abc.txt', 'a+') as file:  # Usando 'a+' adicionamos linhas a um texto existente a cada execução.
#     file.write('Outra linha')
#     print(file.read())

# with open('abc.txt', 'w+') as file:  # Usando 'w+' apaga todo o texto e adiciona nova linha conforme código.
#     file.write('Nova linha')
#     print(file.read())
#
# os.remove('abc.txt')

# Criando e lendo modulo_json.

# d1 será um dicionário comum.

d1 = {
    'Pessoa 1': {'nome': 'Luiz', 'idade': 25},
    'Pessoa 2': {'nome': 'Rose', 'idade': 30},
}

d1_json = json.dumps(d1, indent=True)  # Esse comando converteu o dicionário em modulo_json na variavel d1_json.
print(d1_json)

with open('abc.json', 'w+') as file:  # Agora criamos o arquivo abc.modulo_json e colocamos o conteúdo de d1_json
    file.write(d1_json)

# A leitura desse arquivo foi feito no arquivo ler_json
