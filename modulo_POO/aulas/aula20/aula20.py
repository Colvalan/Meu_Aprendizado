"""
Vamos recriar o funcionamento de uma lista completa usando métodos mágicos que o professor ensinou
"""


# inicio a classe com items entre colchetes vazios, e um index em 0.
class MinhaLista:
    def __init__(self):
        self.__items = []
        self.__index = 0

    # Primeiro método a ser definido será o de adicionar items.
    def __add__(self, valor):
        self.__items.append(valor)

    # Agora vamos implementar um método de exclusão.
    def __delitem__(self, index):
        del self.__items[index]

    # Método de acesso à um item através de seu index.
    def __getitem__(self, index):
        return self.__items[index]

    # Métodos de modificação ou inserção de um item.
    def __setitem__(self, index, valor):
        if index >= len(self.__items):  # Se o index for igual ou maior que o tamanho da lista
            self.__items.append(valor)  # Adiciona o valor usando append (irá pro fim da lista)
        self.__items[index] = valor  # Se não, vai modificar o valor do index que foi mandado na função.

    # Vamos implementar um iterator para que funcione como um 'for' normal.
    def __iter__(self):
        return self

    # Vamos também implementar método para chamar Next, se for preciso.
    def __next__(self):
        try:
            item = self.__items[self.__index]  # Item é igual ao item[index] onde index começa em 0
            self.__index += 1  # Adiciona 1 ao index.
            return item  # Retorna o item
        except IndexError:  # Se consumir todos os indexes existentes, vai levantar IndexError:
            raise StopIteration  # Levanta "StopIteration" porque não há mais indexes a serem mostrados.

    # Método para printar a classe
    def __str__(self):
        return f'{self.__items}'  # Retorna o nome da classe e os items)


if __name__ == '__main__':
    lista = MinhaLista()
    lista.__add__('Kilder')
    lista.__add__('Natalia')
    # del lista[1]  # Apagou 'Natalia'.
    # print(lista[0])  # Printou 'Kilder'.
    # lista[2] = 'Ronaldo'  # adicionou Ronaldo normalmente.
    # lista [0] = 'Colvalan'  # substituiu 'Kilder' por 'Ronaldo' normalmente.
    # for item in lista:
    #     print(item)  # for funcionou como deveria
    # print(next(lista))
    # print(next(lista))
    # print(next(lista))  # No terceiro next, levantou StopIteration, já que só há 2 indexes.