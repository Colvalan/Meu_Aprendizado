"""
Expressão condicional com operador Or.

Parecido com o ternário, é também um atalho para diminuir linhas de códigos desnecessárias.
"""

# Neste exemplo, vou perguntar ao usuário seu nome e mostrá-lo na tela.

# nome = input('Qual é o seu nome?: ')
#
# if nome:
#     print(nome)
# else:
#     print('Você não digitou nada')

# Funcionou perfeitamente, agora, repare no segundo código como farei ele mais curto.

# nome = input('Qual é o seu nome?: ')
# print(nome or 'Você não digitou nada')

# O código acima funcionou exatamente como o código anterior, porém menor.

# Outro exemplo do uso do or

# a = ''
# b = False
# c = None
# d = []
# e = 'Kilder'
#
# variavel = a or b or c or d or e
#
# print(variavel)

# Percebe como or, verificou variavel por variavel, até achar uma que retornasse True, e ai atribuiu o valor a variavel
# Fazendo esse mesmo script usando if, ficaria da seguinte maneira

a = ''
b = False
c = None
d = []
e = 'Kilder'

if a:
    variavel = a
elif b:
    variavel = b
elif c:
    variavel = c
elif d:
    variavel = d
else:
    variavel = e

print(variavel)

# Funciona exatamente como o ultimo código, porém ficou enorme!