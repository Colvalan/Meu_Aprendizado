"""
Funções - def em python (parte 1)
"""
"""


def saudacao(msg='Olá', nome='Usuário'):
    print(msg, nome)


saudacao()
"""

# Vou tentar incorporar meu validador de CPF em uma função def.


def validador():
    cpf = input('Digite o seu cpf (APENAS DÍGITOS): ')
    cpf_sem_digito = cpf[0:9]

    mult = 10
    total = 0

    for valor_cpf in cpf_sem_digito:
        valor_cpf = int(valor_cpf)
        resultado = valor_cpf * mult
        total = total + resultado
        mult = mult - 1

    digito_1 = 11 - (total % 11)

    if digito_1 > 9:
        digito_1 = 0
    else:
        digito_1 = digito_1

    digito_1 = str(digito_1)
    cpf_sem_digito = cpf_sem_digito + digito_1

    mult2 = 11
    total2 = 0

    for valor_cpf2 in cpf_sem_digito:
        valor_cpf2 = int(valor_cpf2)
        resultado2 = valor_cpf2 * mult2
        total2 = total2 + resultado2
        mult2 = mult2 - 1

    digito_2 = 11 - (total2 % 11)

    if digito_2 > 9:
        digito_2 = 0
    else:
        digito_2 = digito_2

    digito_2 = str(digito_2)

    cpf_sem_digito = cpf_sem_digito + digito_2

    sequencia = cpf_sem_digito == str(cpf_sem_digito[0]) * 11

    if cpf_sem_digito == cpf and not sequencia:
        print('Seu CPF é válido')
    else:
        print('Seu CPF é inválido')


print('Boas, vou testar uma função def bem gostosinha.')
print()
print('Basicamente, coloquei meu codigo de validador de cpf em uma função, e vou executá-la aqui.')
print()

usuario = input('Vamos verificar seu cpf? Qual seu nome?: ')

print(f'Boa {usuario}! Vamos verificar esse cpf ai!')
print()

validador()

print(f'Bom demais não é {usuario}?')
