"""
Operador ternário em Python

Funciona como um atalho na hora de definir o valor de uma variável de acordo com condições específicas.
"""

# Verificando usuário logado e liberando ou não acesso.

logged_user = False
msg = 'Usuário logado, pode acessar.' if logged_user else 'Usuário precisa logar para acessar.'

print(msg)

# A variável msg vai receber valor de acordo com condição. No caso do exemplo, se logged_user for true
# a variável msg receberá 'Usuario logado, pode acessar'. Se não, receberá 'Usuário precisa logar pasa acessar.'

