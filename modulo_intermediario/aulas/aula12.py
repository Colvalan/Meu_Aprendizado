"""
Zip - Unindo iteráveis
Zip_longest - Intertools
"""
from itertools import zip_longest  # count

# indice = count()  # Com indice em count, devemos usar zip apenas, para não criar um loop infinito.
# Sem count, podemos usar zip_longest para não perdermos o valor 'monte belo' da lista de cidades.
# Não perderemos 'Monte Belo', mas ele será unido com um valor 'none'
cidades = ['São paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
estados = ['SP', 'BH', 'BA']

cidades_estados = zip_longest(estados, cidades)  # Indice, é uma variavel que vai adicionar index aos valores

for estados, cidades in cidades_estados:  # Valores desempacotados.
    print(estados, cidades)
