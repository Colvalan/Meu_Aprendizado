"""
CPF = 168.995.350-09
_____________________
1 * 10 = 10                     # 1 * 11 = 11
6 * 9 = 54                      # 6 * 10 = 60
8 * 8 = 64                      # 8 * 9 = 72
9 * 7 = 63                      # 9 * 8 = 72
9 * 6 = 54                      # 9 * 7 = 63
5 * 5 = 25                      # 5 * 6 = 30
3 * 4 = 12                      # 3 * 5 = 15
5 * 3 = 15                      # 5 * 4 = 20
0 * 2 = 0                       # 0 * 3 = 0
                                # 0 * 2 = 0
soma dos totais = 297           #
11 - (297 % 11) = x (11)        #  O digito 1 que é igual a 0 foi adicionado apos primeira verificação
x > 9 = 0                       # soma dos totais = 343
x <= 9 = x (11)                 # 11 - (343 % 11) = 9
como 11 é maior que 0 então:    # 9 <= 9 = 9
Digito 1 = 0                    # Digito 2 = 9

Ambos os digitos encontrados pelo algorítmo batem com o CPF digitado pelo usuário, logo ele é valido.
Se não fosse, não seria válido.

Essa é a fórmula do desafio, agora vamos aplicar no python.
"""

# Recebendo cpf e criando variáveis de verificação

cpf = input('Digite o seu cpf (APENAS DÍGITOS): ')
cpf_sem_digito = cpf[0:9]  # Removi os 2 dígitos para que os mesmos sejam obtidos através da fórmula em código.

# Posteriormente, o programa vai verificar se os digitos obtidos batem com o que o usuário informou.

mult = 10
total = 0

# Verificando digito 1.

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

# Digito 1 verificado. Partindo para o digito 2.


digito_1 = str(digito_1)  # Converto o digito verificado em string para concatená-lo ao cpf do usuário.
cpf_sem_digito = cpf_sem_digito + digito_1  # CPF já com dígito 1 concatenado.

# Recomeço a verificação, agora com digito 2.

mult2 = 11
total2 = 0

# Replico o primeiro for apenas mudando o nome das variáveis para 2

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

# Vou converter o digito 2 em string para poder concatená-lo ao restante do cpf

digito_2 = str(digito_2)

# Adiciono o digito 2 no cpf

cpf_sem_digito = cpf_sem_digito + digito_2

# Agora vamos verificar se os digitos obtidos em código batem com o informado pelo usuário.
# Se sim, informo validade, se não,invalidade.

sequencia = cpf_sem_digito == str(cpf_sem_digito[0]) * 11

if cpf_sem_digito == cpf and not sequencia:
    print('Seu CPF é válido')
else:
    print('Seu CPF é inválido')
