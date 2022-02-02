"""
1 - Crie uma função que exibe uma saudação na tela com os parâmetros saudacao e nome.
"""


def exec1(saudacao, nome):
    print(saudacao, nome)


print('Exercício 1:')

exec1('Olá', 'Kilder')
exec1('Hey', 'Natalia!')
print()

"""
2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""

print('Exercício 2:')


def exec2(n1, n2, n3):
    print(n1 + n2 + n3)


exec2(1, 2, 3)
print()

"""
3 - Cria uma função que receba 2 números. O primeiroo é um valor e o segundo um percentual (ex. 10%).
Retorne o valor do primeiro número somado do aumento do percentual do mesmo.
"""

print('Exercício 3')


def exec3(n1, n2):
    return n1 + (n1 * (n2 / 100))


print(exec3(200, 20))
print()

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função
for divisível por 5 retorne Buzz. Se o parâmetro da função for divisível por 5 e 3, retorne Fizz Buzz
caso contrário, retorne o número enviado.
"""

print('Exercicio 4')


def exec4(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return f'{n1} FizzBuzz'
    elif n1 % 3 == 0:
        return f'{n1} Fizz'
    elif n1 % 5 == 0:
        return f'{n1} Buzz'
    else:
        return n1

# Professor sugeriu adicionar números randomicos.


for sequencia in range(100):
    print(exec4(sequencia))
