"""
Funções (def) em python - return. Parte 2.
"""


"""
def funcao(var):
    return var


variavel = funcao('valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')
"""

# Exemplo de função matemática com condição.


def divisao(n1, n2):
    if n2 == 0:
        return
    else:
        return n1 / n2


conta = divisao(7, 0)

if conta:
    print(conta)
else:
    print('Conta Invalida')

