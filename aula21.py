"""
Try e Except como condicional
"""


def conversor(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except:
            pass


while True:
    numero = conversor(input('Digite um número: '))

    if numero is None:
        print('Erro: Isso não é um número')
    else:
        print(numero * 2)
