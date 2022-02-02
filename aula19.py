"""
Try - Except
"""
try:
    print(a)
except:
    print('Erro')

try:
    print(a)
except NameError as erro:
    print(erro)

try:
    a = 1 / 0
except ZeroDivisionError:
    print('Impossível dividir por 0')

# aplicação em uma calculadora

print('Programa de divisão')
div = int(input('Digite um número: '))
div2 = int(input('Digite otro número: '))

try:
    print(div / div2)
except ZeroDivisionError:
    print('Impossível dividir por 0.')

# Programa encerrou sem que o erro apareça na tela e o código seja interrompido.