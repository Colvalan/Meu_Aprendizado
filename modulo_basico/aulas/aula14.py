# Esta aula ficou confusa, o professor quis mostrar sobre a documentação do python.
# Porém, com os comandos que ele mostrou, não foi capaz de resolver o proprio problema proposto.
# O problema se trata de uma calculadora que não consegue funcionar caso o usuário digite uma letra
# ao invés de um número. Ele propos resolver o problema com comando "Try" que pede que o python
# tente rodar uma parte do código, que, casa haja erro, crie uma excessão ao invés de um crash.
# O exemplo ficou assim:

num1 = input('digite um numero: ')
num2 = input('digite outro numero: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERRO')
