"""
Enum, é usado quando precisamos de um "pacote" de condições.
No exemplo abaixo, vamos usar Enum, em um codigo que representa um game onde movimentamos o personagem.
Ao invés de usar 'If' para verificar cada direção, vamos usar Enum.
"""
from enum import Enum, auto

# Criaremos uma classe para definir as direções possiveis a se mover, que vai herdar de Enum.


class Directions(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()


def move(direction):  # Função que recebe uma direção, que vira de Directions.
    if not isinstance(direction, Directions):  # Se não for umas instancia de Directions
        raise ValueError('Cannot move in this direction')  # Levanta esta exceção.

    return f'Moving {direction.name}'  # Retorno da função.


if __name__ == '__main__':
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    # print(move('bla'))  # Qualquer coisa que não for umas instancia de Directions, levanta ValueError

# Para atingirmos esse resultado sem Enum, teriamos que verificar as direções com if, todas elas.
# Teriamos algo como:

print('_______________________________')


def move1(direction):
    if direction != 'right' and direction != 'left' and direction != 'up' and direction != 'down':
        raise ValueError('Cannot move in this direction')
    return f'Moving {direction}'



print(move1('right'))
print(move1('left'))
print(move1('up'))
print(move1('down'))
print(move1('bla'))  # Levanta exceção.

# Na linha 40, verifiquei se direção se enquadra no que precisamos, caso não, levanta exceção
# Porém, o if fica muito grande, isso que só usamos 4 direções, quando podem ser várias.
# Para isso serve o Enum, colocamos as direções possiveis dentro dessa classe.
# Se o que a função receber não estiver na classe Directions que herda de Enum, vai levantar exceção.
# Isso deixa o código mais facil de ser lido e mais enxuto.
