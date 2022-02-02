horario = input('Que horas são? (formato HH): ')

try:
    horario = int(horario)
    if horario < 0:
        print('Digite um horário no formato HH válido!')
    elif horario == 0 or horario <= 11:
        print('Bom dia!')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde!')
    elif horario >= 18 and horario <= 23:
        print('Boa noite!')
    else:
        print('Digite um horário válido')
except:
    print('Digite um horário no formato HH válido!')

'''
    Considerações Finais.
    
    O exercício foi codado corretamente e eu obtive o mesmo resultado que o professor, com algumas diferenças
lógicas.
    
    O professor fez o programa da seguinte maneira:

horario = input('Digite um horário (0-23): ')

# Aqui ele verificou se o que foi digitado pelo usuário é um numero, se sim, faz cast para int.

if horario.isdigit():
    horario = int(horario)
    
# Aqui ele determinou que se for menor que 0 ou maior que 23, o programa retorna "Horario deve estar entre 0 e 23"
    
    if horario < 0 or horario > 23:
        print ('Horario deve estar entre 0 e 23')
        
# Se não que o programa prossiga com as verificações.

    else:
        if horario <= 11:
             print('Boa dia!')
         elif horario <= 17:
             print('Boa tarde!')
         else:
             print('Boa noite!')

# Para fechar o primeio if, se o usuário digitar um numero fora dos limites de 0 a 23 ou uma letra, o programa retorna:             

else:
     print("Por favor, digite um horário entre 0 e 23.")
'''