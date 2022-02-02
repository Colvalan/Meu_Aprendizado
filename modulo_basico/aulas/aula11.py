"""
Operadores relacionais
== - Igual que
> - Maior que
>= - Maior ou igual que
< - Menor que
<= - Menor ou igual que
!= - Diferente que
"""

# se fosse verificação com minimo de idade para empréstimo em 18 anos.

# nome = input('Qual o seu nome? ')
# idade = int(input('Qual a sua idade? '))
#
# if idade > 18:
#    print(f'Olá {nome}! Você é maior de idade e pode pegar um empréstimo')
# else:
#   print(f'Olá {nome}! Infelizmente você é menor de idade e não pode pegar um empréstimo')

# programa feito levando em conta idade minima de 20 e máxima em 30 para empréstimo
# não considerando o comando "and"

# nome = input('Qual o seu nome? ')
# idade = int(input('Qual a sua idade? '))
#
# if idade < 20:
#     print(f'Olá {nome}! Você é muito jovem para pegar um empréstimo')
# elif idade == 20:
#     print(f'Olá {nome}! Você pode pegar um empréstimo!')
# elif idade <= 30:
#     print(f'Olá {nome}! Você pode pegar um empréstimo!')
# elif idade > 30:
#     print(f'Olá {nome}! Infelizmente um empréstimo não está disponível')

# refazendo o programa considerando o comando "and" (and foi aplicado na linha 44 porém o Pycharm
# sugeriu uma comparação simplificada aplicando 20 <= idade <= 30 o que funcionou da mesma maneira.

# nome = input('Qual é o seu nome? ')
# idade = int(input('Qual é a sua idade? '))
#
# if idade < 20:
#     print(f'Olá {nome}! Infelizmente não temos um empréstimo disponível para você')
# elif 20 <= idade <= 30:
#     print(f'Olá {nome}! Temos um empréstimo disponível para você!')
# else:
#     print(f'Olá {nome}! Infelizmente não temos um empréstimo disponível para você')
