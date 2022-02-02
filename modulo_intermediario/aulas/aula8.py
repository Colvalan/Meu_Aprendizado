"""
Sistemas de perguntas e respostas com dicionários
"""

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Qual é meu game favorito?',
        'respostas': {'a': 'PUBG', 'b': 'Simulador', 'c': 'Pacman'},
        'resposta certa': 'a'
    },
    'Pergunta 2': {
        'pergunta': 'Quem eu amo mais?',
        'respostas': {'a': 'Minha moto', 'b': 'Meu PC', 'c': 'Meu Doguinho'},
        'resposta certa': 'c'
    },
    'Pergunta 3': {
        'pergunta': 'O que mais gosto de comer?',
        'respostas': {'a': 'Churrasco', 'b': 'Lasanha', 'c': 'Pipoca'},
        'resposta certa': 'c'
    },
    'Pergunta 4': {
        'pergunta': 'Qual joguin novo to jogando agora?',
        'respostas': {'a': 'Nanny People', 'b': 'Super People', 'c': 'Village People'},
        'resposta certa': 'b'
    }
}
print('Provinha sobre o Kilder!')

respostas_certas = 0

for pergunta_chave, pergunta_valor in perguntas.items():
    print()
    print(f'{pergunta_chave}: {pergunta_valor["pergunta"]}')
    print()
    for resposta_chave, resposta_valor in pergunta_valor['respostas'].items():
        print(f'[{resposta_chave}] {resposta_valor}')

    print()
    resposta_usuario = input('Qual é a sua resposta: ')
    if resposta_usuario == pergunta_valor['resposta certa']:
        print()
        print('Você acertou!')
        respostas_certas = respostas_certas + 1
    else:
        print()
        print('Você Errou!')

porcentagem_de_acerto = respostas_certas / len(perguntas) * 100

print()
print(f'Você acertou {respostas_certas} perguntas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_de_acerto}%')
