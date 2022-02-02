"""
While / Else
contadores
acumuladores
"""

contador = 1
acumulador = 1

while contador <= 10:
    print(contador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador = contador + 1
else:
    print('Cheguei no else')

print('Else não executado devido linha de break')

'''
Essa aula foi apenas um exemplo de lógica de contador com acumulador
Também usamos else com while que em algumas linguagens não é possível.
'''