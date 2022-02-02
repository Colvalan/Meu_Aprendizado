"""
Esse exercício, foi bem dificil pra mim no inicio. Penei muito para conseguir fazer.
Depois de passar por muitos novos conhecimentos, decidi rever esse exercicio sem consultar o antigo.
Montei uma logica na cabeça e tentei replicar no código, foi dificil mas consegui e me ajudou a exercitar meu raciocínio
lógico. O código ficou melhor, com mais funcionalidades e melhorias. Código mais fácil de ler e mais eficiente.
Fiquei satisfeito com o resultado, ainda demoro demais para colocar em prática uma lógica, mas meu raciocínio ainda
vai melhorar bastante com o tempo.

Ainda falta eu comentar o código, será feito posteriormente, quero treinar minha capacidade de entender códigos meus
depois de um tempo. Isso vai ajudar a melhorar minhas compreensão sobre as sintaxes e lógicas do python.

Para consultar minha primeira tentativa para um programa de forca, conferir:
"/modulo_basico/exercicios_modulo_basico/meu_jogo_de_adivinhacao"
"""

palavra_secreta = 'kil'
secreta_escondida = ['*' for x in palavra_secreta]
chances = 5
i = 0
repetidos = []

print('Jogo de forca! A palavra tem', len(palavra_secreta), 'letras e você pode errar até 5 vezes!')
print('Use apenas letras minúsculas. Letras maíusculas contará como um erro!.')
print()

while chances != 0:

    if chances >= 1:
        print('Por enquanto está assim : ', *secreta_escondida, sep='')
        print()
        letra = input('Tente uma letra: ')
        if letra not in repetidos:
            repetidos.append(letra)
        else:
            print('Essa letra você já digitou! Tente novamente.')
            continue

        if len(letra) > 1:
            chances -= 1
            print(f'Digitar mais de 1 caractere é trapaça! Por isso agora você só tem mais {chances} chances!')
            print()
            continue

        for x in range(len(palavra_secreta)):

            if letra == palavra_secreta[x]:
                secreta_escondida[x] = letra
                if '*' not in secreta_escondida:
                    print(f'Você venceu! A palavra era {palavra_secreta}.')
                    print()
                    print('Obrigado por jogar!')
                    exit()

        if letra not in palavra_secreta:
            chances = chances - 1
            if chances != 0:
                print(f'Você errou e ainda pode errar mais {chances} vezes.')
                print('Letras já digitadas:', *repetidos, sep=' ')
                print()
                continue
            else:
                print()
                print('Você perdeu!')
                print('Obrigado por jogar!')
                exit()

        print('Você acertou uma letra!')
        print('Letras já digitadas:', *repetidos, sep=' ')
        print()
