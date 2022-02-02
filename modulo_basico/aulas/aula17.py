"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings) - (?)
:d - Inteiros (int) - (?)
:f - Números de ponto flutuante (float) - Exemplo 2
:. (NÚMERO) f - Quantidade de casas decimais (float) - Exemplo 2
: (CARACTERE) (> ou < ou ^) QUANTIDADE (TIPO - s, d ou f) - Exemplo 1

> - Esquerda
< - Direita
^ - Centro
"""

# Exemplo 1 - formatei a variável nome para ter 10 caractéres e que complete o restante com @ a direita.


nome = 'Kilder'

print(f'{nome:@<10}')

# Exemplo 2 - irei formatar uma variavel tipo float para ter 2 casas decimais.

"""
num1 = 10
num2 = 3
div = num1 / num2

print(f'{div:.2f}')  # Sem esta formatação, seria impresso 3.33333333335
"""

# Exemplo 1 agora utilizando .format
"""
nome = 'Kilder'
nome_formatado = '{:@>50}'.format(nome)
# Acima, formatei a var nome para ter 50 caracteres, e que complete os caracteres com @ a esquerda do nome.
# Logo foi impresso: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Kilder
print(nome_formatado)
"""