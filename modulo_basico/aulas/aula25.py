"""
For / Else
"""

# Exemplo contido em documentação no caderno.
# Neste exemplo de else com for, apenas mostra como o for verificou se um valor da lista começa com N
# Se sim, continua o laço sem impressão, se não (else) imprime o valor.

lista = ['Kilder', 'Natalia', 'Eliana']

for pessoa in lista:
    if pessoa.startswith('N'):
        continue
    else:
        print(pessoa)

# Exemplo contido em documentação no caderno.
# Neste exemplo, mostra apenas como o for itera sobre a lista para definir a variável pessoa.

lista = ['Kilder', 'Natalia', 'Eliana']

for pessoa in lista:
    print(pessoa)
