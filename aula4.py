"""
parte 4

escopo de variável
"""

# Uma variável criada antes de uma função tem seu escopo como global. Uma variavel criada dentro de uma função
# tem seu escopo como interno. Segue exemplo...

# var = 'Kilder'
#
#
# def func():
#     print(var)
#
#
# def func1():
#     var = 'Ronaldo'
#     print(var)
#
#
# func()
# func1()

"""
No exemplo acima, apesar da variavel 'var' ter o mesmo nome dentro e fora da função func1, o que prevalece fora
dessa função é o valor dado antes dela ou seja 'Kilder' porque esse valor foi dado a ela em um escopo global.
Por isso, o valor 'Ronaldo' só vale a para 'var' que está dentro de func1 devido seu escopo interno.
"""

# Agora vamos usar o comando 'global' para forçar uma var dentro da func ter seu escopo global.

# var = 'Kilder'
#
#
# def func():
#     print(var)
#
#
# def func1():
#     global var
#     var = 'ronaldo'
#     print(var)
#
#
# func()
# func1()
#
# print(var)

"""
Nesse exemplo acima, a variável "var" a partir da func1 teve seu escopo forçado a global pelo comando 'global'
Isso faz com que seu valor dado dentro da função 'ronaldo' seja carregado para fora da função em todo o códido.
Porém, essa pratica não é boa considerada pela comunidade do python já que pode causar confusão e comportamento
ruim do código. Nesses casos, o ideal é trabalhar o valor da variavel dentro da função para que ela retorne um valor
apeenas dentro dessa função, veja o exemplo abaixo.
"""

# var = 'Kilder'
#
#
# def func():
#     print(var)
#
#
# def func1():
#     arg = var.replace('K', 'W')
#     return arg
#
#
# func()
# var_nova = func1()
#
# print(var_nova)

"""
Também não é possível tentar usar a variavel de uma função que tem seu escopo como local, em uma outrar variável.
Se tentar fazer isso, vai gerar um erro:
"""


# def func():
#     var = 'Kilder'
#     print('Kilder')
#
#
# def func1():
#     print(var)
#
#
# func()
# func1()

"""
Para corrigir isso, devemos retornar o valor da variável na função, e chamar essa função em uma outra, ai sim
da certo, veja exemplo:
"""


def func():
    var = 'Kilder'
    return var


def func1(arg):
    print(arg)


var = func()
func1(var)

"""
No exemplo acima, defini a variavel na primeiro função e pedi para retornar o valor dela em "var"
Na segunda função, dei o print em um argumento.
Depois, fora da função, defini o valor de 'var' como o que foi retornado da primeira função
E por ultimo, usei a func1 que tem como utilidade o comando print, e seu argumento foi 'var'
Dessa maneira, pude interlidar 2 funções usando a mesma variavel.
"""