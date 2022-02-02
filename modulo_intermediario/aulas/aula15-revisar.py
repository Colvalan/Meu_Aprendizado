"""
Como agrupar elementos no python com Groupby
"""

from itertools import groupby

lista = [
    {'Nome': 'Kilder', 'Nota': 'A'},
    {'Nome': 'Ronaldo', 'Nota': 'C'},
    {'Nome': 'Julia', 'Nota': 'D'},
    {'Nome': 'Anderson', 'Nota': 'B'},
    {'Nome': 'Vinicius', 'Nota': 'B'},
    {'Nome': 'Caio', 'Nota': 'A'},
    {'Nome': 'Natalia', 'Nota': 'C'},
    {'Nome': 'Edson', 'Nota': 'D'},
    {'Nome': 'Eliana', 'Nota': 'A'},
    {'Nome': 'Danilo', 'Nota': 'B'},
]

ordenacao = lambda item: item['Nota']
lista.sort(key=ordenacao)
alunos_agrupados = groupby(lista, ordenacao)

for notas, notas_agrupadas in alunos_agrupados:
    print(f'Notas: {notas}')

    quantidade = (len(list(notas_agrupadas)))
    print(f'{quantidade} alunos tiraram a nota {notas}')
