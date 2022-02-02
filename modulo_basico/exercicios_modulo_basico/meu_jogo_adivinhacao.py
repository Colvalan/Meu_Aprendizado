"""
Vou tentar replicar o jogo de adivinhação do professor sem copiar nem consultar o código dele
"""

# Minha palavra secreta será "kilder"
# Irei criar uma lista vazia para armazenar as letras conforme elas forem adivinhadas corretamente
# O número de chances será de 5. O usuário poderá errar a adivinhação 5 vezes.

palavra_secreta = 'kilder'
lista_letras_digitadas = []
chances = 5

# Usando while para que o programa funcione até uma determinada condição que exista um break.

while True:

    # Verificando chances, se for menor ou igual a 0, o jogo avisa que o usuário perdeu e encerra o programa
    # com comando "break"

    if chances <= 0:
        print('Você perdeu')
        break

    # Vou pedir uma letra ao usuário

    letra_digitada = input('Digite uma letra: ')

    # Verificando se o usuário digitou mais de 1 caracter, se sim, peço uma letra apenas e reinicio o while
    # com o comando "continue". Se não, o programa continua.

    if len(letra_digitada) > 1:
        print('isso não vale, digite apenas uma letra!')
        continue

    # Verificando se o que foi digitado é maiusculo, se sim, converter a minusculo

    if letra_digitada.isupper():
        letra_digitada = letra_digitada.lower()

    # Verificando se a letra digitada está na palavra secreta, se sim, adiciona ela na lista e avisa
    # o usuário que ele adivinhou uma letra. Se não, não adiciona na lista e avisa o usuário que a letra
    # digitada não existe na palavra secreta

    if letra_digitada in palavra_secreta:
        lista_letras_digitadas.append(letra_digitada)
        print(f'Você adivinhou umas das letras! A letra "{letra_digitada}" faz parte da palavra secreta!')
    else:
        print(f'Você errou, a letra "{letra_digitada}" não faz parte da palavra secreta')

    # Vou criar uma palavra secreta incompleta, que mostrará as letras adivinhadas em sua posição correta
    # e o que ainda não tiver sido adivinhado, será mostrado como '*'

    palavra_secreta_incompleta = ''

    # o laço "for", vai criar uma variável letra_secreta_incompleta que será montada a partir da verificação de
    # indice por indice da variável palavra_secreta

    for letra_secreta_incompleta in palavra_secreta:

        # Se a letra incompleta estiver na lista de letras digitadas, irá preencher a palavra_secreta_incompleta
        # com a mesma, se não, será preenchido com '*'.

        if letra_secreta_incompleta in lista_letras_digitadas:
            palavra_secreta_incompleta = palavra_secreta_incompleta + letra_secreta_incompleta

        else:
            palavra_secreta_incompleta = palavra_secreta_incompleta + '*'

    # Neste momento, se a palavra_secreta_incompleta estiver == a palavra secreta, avisa o usuário que ele venceu
    # e quebra o while com break, se não, mostra como a palavra_secreta_incompleta está no momento

    if palavra_secreta_incompleta == palavra_secreta:
        print(f'Você ganhou! A palavra secreta era "{palavra_secreta}"')
        break
    else:
        print(f'A palavra secreta no momento está assim: {palavra_secreta_incompleta}')

    # Se a letra que foi digitada pelo usuário estiver na palavra secreta, não subtrair suas chances
    # e mostrar quantas chances ele ainda possui. Se não, subtrair uma chance, e avisá-lo de quantas
    # chances ele possui depois dessa subtração.

    if letra_digitada in palavra_secreta:
        print(f'Você ainda tem {chances} chances.')
        print()
    else:
        chances = chances - 1
        print(f'Você agora tem {chances} chances')
        print()

# O while recomeçara até que o usuário complete a palavra, quando esse momento chegar o programa será suspenso
# com o "break" da linha 74. Se suas chances acabarem, o programa será encerrado com o "break" da linha 22.

'''
Consegui replicar o programa do professor sem nenhum tipo de consulta ou cópia de seu código, e me sinto muito
orgulhoso de tal feito, afinal, essa lógica foi dificil de entender devido laço "for" que ainda não está 100%
claro na minha mente.

Basicamente esse laço "for" foi usado para criar uma palavra com o mesmo número de caracteres da palavra secreta
mas representada por '*' em caracteres que ainda não tivessem sido adivinhados. Ou seja para a palavra secreta
kilder, foi criado uma representação dela em * que ficou ******. Conforme o "for" verificava os indices da palavra
secreta, caso uma letra já estivesse na lista de letras digitadas, ao inves de preencher os indices com *,
preenchia com a letra em si. Então quando chegava por exemplo no "i" de "kilder", ele verificava se i estava
na lista de letras digitadas, e se o i estivesse la, preenchia o i com a letra i ao invés de * ficando *i****

Isso foi útil para mostrar ao usuário o seu progresso e que ele pudesse adivinhar a palavra fazendo uma previsão
com base no que ja tivesse sido adivinhado.

Isso foi bastante complicado de entender e me impressionou o professor criar essa logica pelo menos nesse momento
bastante complexa para mim, de maneira tão natural e rapida.

Ainda estou no começo mas sinto que meu pensamento lógico ainda é um bocado fraco, mas sei que vai evoluir.
'''