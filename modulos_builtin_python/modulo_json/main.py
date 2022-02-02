"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""
from dados import *
import json

# Abaixo, vamos converter um dicionario python, em modulo_json, e salvar esses dados em uma var chamada dados_json.

# dados_json = modulo_json.dumps(clientes_dicionario, indent=4)
# print(dados_json)

# --------------------------------------------------------------------------------------------------------

# Abaixo, carregamos uma var que contem uma string com dados modulo_json, e a trarnsformamos em um objeto python.
# Prova disso, que pudemos fazer um for no que foi convertido.

# dicionario = modulo_json.loads(clientes_json)
# for chave, valor in dicionario.items():
#     print(chave, valor)

# --------------------------------------------------------------------------------------------------------

# Abaixo, criamos um arquivo modulo_json chamado 'clientes_json' com instrução de escrita, e usamos modulo_json.dump.
# na assinatura de modulo_json.dump, veio primeiro o dicionario em python, mandamos o arquivo que criamos, com indentação em 4
# Isso criou um arquivo com estrura modulo_json a partir de um dicionario em python.

# with open('clientes.modulo_json', 'w') as arquivo:
#     modulo_json.dump(clientes_dicionario, arquivo, indent=4)

# --------------------------------------------------------------------------------------------------------

# Agora, vamos abrir o arquivo criado anterior, com instrução de leitura.
# E partir dos dados modulo_json contidos em 'clientes.modulo_json', criamos uma variavel.
# Essa variavel recebeu os valores em modulo_json, e criou um dicionario em python como estes dados
# Prova disso, que pudemos iterar sobre essa variavel.

# with open('clientes.modulo_json', 'r') as arquivo:
#     dados = modulo_json.load(arquivo)
#
# for chave, valor in dados.items():
#     print(chave, valor)
