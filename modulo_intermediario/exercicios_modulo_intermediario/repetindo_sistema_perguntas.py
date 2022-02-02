"""
Esse exercício, eu consegui fazer mas não sozinho, precisei ler e reler varias vezes o código do professor
para entender a lógica usada.
Depois de estudar o que foi feito no código, decide repetir o exercicio mas agora sem consultar ou copiar código.
Resultado satisfatório!
"""

print('Provinha de noia')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quem é hoje, o presidente do brasil?',
        'respostas': {'a': 'Jair Biruliro', 'b': 'Jair Bonoro', 'c': 'Jair Bolsonaro'},
        'resposta certa': 'c'
    },
    'Pergunta 2': {
        'pergunta': 'Quem é o atual campeão mundial de Fórmula 1?',
        'respostas': {'a': 'Cristiano Ronaldo', 'b': 'Max Verstappen', 'c': 'Lebron James'},
        'resposta certa': 'b'
    },
    'Pergunta 3': {
        'pergunta': 'Qual é o país do futebol?',
        'respostas': {'a': 'Brasil', 'b': 'Estônia', 'c': 'Jamaica'},
        'resposta certa': 'a'
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 3 + 2 x 4?',
        'respostas': {'a': '20', 'b': '11', 'c': '14'},
        'resposta certa': 'b'
    },
    'Pergunta 5': {
        'pergunta': 'Em briga de aleijado, quem vence?',
        'respostas': {'a': 'O que não tem braço', 'b': 'O que não tem perna', 'c': 'Empate'},
        'resposta certa': 'c'
    },
    'Pergunta 6': {
        'pergunta': 'Se foi sem querer querendo, quem bateu?',
        'respostas': {'a': 'Chaves', 'b': 'Chapolin', 'c': 'Chiquinha'},
        'resposta certa': 'a'
    },
    'Pergunta 7': {
        'pergunta': 'Considerando que macaco curte banana, gato curte oq?',
        'respostas': {'a': 'Rato', 'b': 'Mexirica Poncán', 'c': 'Batata'},
        'resposta certa': 'a'
    }
}

respostas_certas = 0

for pc, pv in perguntas.items():
    print()
    print(f'{pc}: {pv["pergunta"]}')
    print()
    for rc, rv in pv['respostas'].items():
        print(f'[{rc}] {rv}')

    print()
    resposta_usuario = input('Qual é a sua resposta: ')

    if resposta_usuario == pv['resposta certa']:
        print('Você acertou.')
        respostas_certas = respostas_certas + 1
    else:
        print('Você errou.')

porcentagem_de_acertos = respostas_certas / len(perguntas) * 100

print()
print(f'Você acertou {respostas_certas} perguntas')
print(f'Sua porcentagem de acerto foi de {porcentagem_de_acertos:.2f}%')
