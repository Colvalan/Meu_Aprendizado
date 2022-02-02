"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.

NÃO CONSEGUI FAZER! NECESSITA REVISÃO
"""


# def ola_mundo():
#     return 'Olá mundo!'  # Apenas uma função que retorna a string 'Olá mundo!'
#
#
# def mestre(funcao):
#     return funcao()  # Função que recebeu uma função executada.
#
#
# executando = mestre(ola_mundo)  # Variável == função mestre que recebeu como parâmetro a funçãoo olá_mundo.
# print(executando)  # Print da função 1 executada.

"""
2 - Crie uma função mestre que retorne uma função executada. Crie 1 função que recebe 1 argumento, e 1 função
que receba 2 argumentos. Faça ambas funções serem executadas na função mestre.

NÃO CONSEGUI FAZER, NECESSITA REVISÃO
"""


def mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)


def oi_pessoa(nome):
    return f'oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'


executando = mestre(oi_pessoa, nome='Kilder')
executando1 = mestre(saudacao, nome='Kilder', saudacao='Eae')

print(executando)
print(executando1)
