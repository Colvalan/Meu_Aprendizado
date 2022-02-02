numero = input('Digite um número inteiro: ')

try:
    numero = int(numero)
    resto = numero % 2
    if resto == 0:
        print(f'{numero} é numero par')
    else:
        print(f'{numero} é numero impar')
except:
    print('ERRO: ISSO NÃO É UM NÚMERO INTEIRO.')

'''
Considerações finais:

O execício foi corretamente codado com algumas diferenças em relação á resolução do professor

Nesse caso específico ele resolveu da seguinte maneira:

numero_inteiro = input('Digite um número inteiro: ')

if not numero_inteiro.isdigit():  # Aqui ele verificou se o usuário digitou realmente um número usando var.isdigit().
    print('Isso não é um número inteiro')
else:  # Caso o usuário tenha digitado um numero válido, faz o cast para int:
    numero_inteiro = int(numero_inteiro)
    
        if not numero_inteiro % 2 == 0:  # Se o numero digitado não tiver o módulo de 2 == a 0 o numero é impar.
            print(f'{numero_inteiro} é ímpar')
        else:
            print(f'{numero_inteiro} é par')
            
    O método do professor funcionou exatamente como o meu, mas com um porém,
quando digitado um número negativo pelo usuário o programa retorna "Isso não é um número inteiro",
o que está matematicamente incorreto, porém, ele deve ter feito assim por alguma razão.

    A minha resolução trata também numeros negativos, e retorna se os mesmos são impar ou par já que
numeros negativos também são inteiros.
'''