"""
Comma Separated Values - CSV (valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de dados,
clientes de e-mail e etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]  # Criamos uma lista a partir do gerador

with open('clientes2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',  # O que define onde cada valor termina. CSV no caso, são virgulas.
        quotechar='"',  # O que será usado como aspas. No caso, aspas duplas.
        quoting=csv.QUOTE_ALL  # Comando para que todos os valores estejam entre aspas.
    )

    # Agora vamos adicionar o cabeçalho ao novo arquivo.

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],  # Chave 'Nome'
            chaves[1],  # Chave 'Sobrenome'
            chaves[2],  # Chave 'E-mail'
            chaves[3]   # Chave'Telefone'
        ]
    )

    for dado in dados:  # Esse for, vai escrever linha por linha composta de:
        escreve.writerow(
            [
                dado['Nome'],  # O valor de nome
                dado['Sobrenome'],  # O valor de Sobrenome
                dado['E-mail'],  # O valor de E-mail
                dado['Telefone']  # O valor de Telefone
            ]
        )
