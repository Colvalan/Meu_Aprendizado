"""
Manipulando strings
* String Indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em casa tipo.

Você pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipos de built-in)
https://docs.python.org/3/library/functions.html (funções built-in)
"""
# String Indices

# positivos  012345
"""
nome      = 'Kilder'
# negativos  654321

url = 'www.google.com.br/'

print(url[:-1])  #esse comando entre colchetes determinou que a var "url" fosse impressa sem o indice -1
"""
# no caso da var url, o indice -1 é a barra ao final do link.

# Fatiamento de string

#       012345678901234 - positivo apenas, a partir do segundo zero, considerar 10 11 12...
nome = 'Kilder Colvalan'
nome_fatiado = nome[0:15:2]
print(nome_fatiado)
