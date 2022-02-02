"""
Desafio dos dois contadores. Devo usar for ou while.

0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

# contador1 = 0
# contador2 = 10
#
# while True:
#
#     if contador1 <= 8 and contador2 <= 10:
#         print(contador1, contador2)
#         contador1 = contador1 + 1
#         contador2 = contador2 - 1
#     else:
#         break

'''
Percebi como ainda preciso melhorar muito, e lembrar de algumas funções
Apesar de ter resolvido o problema passado pelo professor, ele conseguiu fazer o mesmo em 2 linhas
O que é mais eficiente e facil, e fez me sentir um completo idiota.
'''

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)

'''    
O for foi utilizado por se saber quando será o final do laço. "p" é o enumerate, enumerando cada laço
O r, é o contador usando função range com inicio no 10, final no 1 ou seja, até o 2, e pulo -1, isso fez
com que a função range contasse do ultimo numero para o primeiro.
'''
'''
o enumerate começou do 0, e o primeiro valor de r, é 10, por isso começou com 0 10
o segundo laço foi enumerado com 1, e o segundo valor de r foi 9, e por isso 1 9
Seguindo essa lógica, o laço foi até r valer 2, e o enumerate enumerou todos os 9 laços.
Dando a sequencia que ele pediu.
Agora ficou super óbvio o que ele fez, mas antes, jamais teria pensado nisso.
'''
'''
Ridículamente esperto, estou no inicio dos estudos e jamais teria feito dessa maneira.
Triste, mas devo continuar animado, isso serve de experiencia, as vezes só resolver o problema não basta!
'''