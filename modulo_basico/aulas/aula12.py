"""
Operadores lógicos
and, or, not
in e not in
"""
# Operador And, as duas comparações precisam ser verdadeiras para retornar True.
# Uma delas sendo falsa, retornara False
# (verdadeiro e verdadeiro) - True
# (verdadeiro e falso) - False
# comparacao1 and comparacao2

# Neste exemplo, vai retornar false já que 2 < 4 mas 2 não é > 4.

"""
a = 2
b = 4
if a < b and a == b:
    print('true')
else:
    print('false')
"""

# Neste exemplo, vai retornar true por que 2 < 4 e 2 <= 4.

"""
a = 2
b = 4
if a < b and a <= b:
    print('true')
else:
    print('false')
"""

# Operador Or, ou uma ou outra precisa ser verdadeira para retornar True.
# Só retornará false se ambas forem falsas.
# (Verdadeiro ou verdadeiro) - True
# (Verdadeiro ou falso) - True
# (falso ou falso) - False
# comparacao1 or comparacao2

# Neste exemplo, retornara true por que 2 < 4 e isso já basta.

"""
a = 2
b = 4
if a < b or a <= b:
    print('true')
else:
    print('false')
"""

# Neste exemplo, retornará false porque 2 não é > 4 e 2 não é >= 4. Ambas são falsas.

"""
a = 2
b = 4
if a > b or a >= b:
    print('true')
else:
    print('false')
"""

# Operador not funciona como um inversor, invertendo o que a comparação retornaria
# Se true, inverte a false, se false, inverte a true.

# Neste exemplo vai retornar false, mesmo que 2 < 4 esteja correto.

"""
a = 2
b = 4
if not a < b:
    print('true')
else:
    print('false')
"""

# Neste exemplo, vai retornar true mesmo que 2 > 4 esteja errado.

"""
a = 2
b = 4
if not a > b:
    print('true')
else:
    print('false')
"""

# Operador in serve para conferir de uma letra ou numero está presente em uma variável

# neste exemplo, retornara 'não existe "il" em nome' ja que "il" não existe na string 'colvalan':

"""
nome = 'Colvalan'
if 'il' in nome:
    print('Existe "il" em nome')
else:
    print('Não existe "il" em nome')
"""

# Neste exemplo, retornara 'Existe "il" em nome' porque "il" existe na string 'Kilder'

"""
nome = 'Kilder'
if 'il' in nome:
    print('Existe "il" em nome')
else:
    print('Não existe "il" em nome')
"""

# Operador not in funciona como o in porém invertido, já que une as funções de In e Not.

# Nesse exemplo, o python vai executar o else mesmo contendo 'il' em 'Kilder', e retornar "Não existe 'il' em nome.

"""
nome = 'Kilder'
if 'il' not in nome:
    print('Existe "il" em nome')
else:
    print('Não existe "il" em nome')
"""

# Nesse exemplo ocorrerá o contrário.
"""
nome = 'colvalan'
if 'il' not in nome:
    print('Existe "il" em nome')
else:
    print('Não existe "il" em nome')
"""

# Exemplo de uso do operador and em uma aplicação com login e senha

usuario = input('Qual é o nome do usuário: ')
senha = input('Qual é a senha do usuário: ')

usuario_bd = 'kilder'
senha_bd = 'kilder410'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos')
