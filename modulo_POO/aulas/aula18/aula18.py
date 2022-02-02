"""
O que são dataclasses? O módulo Dataclasses fornece um decorador e funções
para criar automaticamente métodos, como __init__(), __repr__(), __eq__() e etc
em classes definidas pelo usuário.
Basicamente, dataclasses são sytax sugar para criar classes normais.
Foi originalmente descrito no PEP 557.
Adicionado na versão 3.7 do Python.
Leia a documentação em: https://docs.python.org/pt-br/3/library/dataclasses.html
"""
from dataclasses import dataclass
from dataclasses import field
from dataclasses import asdict, astuple


# O que vai entre parenteses não métodos que dataclasses já cria automaticamente para nós.
# Podemos deixá-las padrão, ou não. Para mudar seus padrões, mandamos instruções no parenteses.
# eq = Sobrecarda do operação ==.
# repr = Maneira como o python printa nossos objetos.
# order = Métodos que ordena nossas instancias por atributo x ou y.
# frozen = Congela a classe após o init.
# init = Iniciador da classe.

@dataclass(eq=True, repr=True, order=True, frozen=False, init=True)
class Pessoa:
    nome: str
    sobrenome: str = field(repr=False)  # Se mudar para True, isso omite sobrenome no repr.

    # Post init é executado após init. Poderia definir atributo ou filtrar atribuitos anteriores
    # conforme exemplo.

    def __post_init__(self):
        if not isinstance(self.nome, str):
            raise TypeError(
                f'Tipo inválido {type(self.nome).__name__} != str em {self}')

    # Dataclasse funciona exatamente como uma classe normal, portanto, posso definir métodos
    # com ou sem Getters e Setters.

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

# Usando método "order" com lambda.


p1 = Pessoa('A', '5')
p2 = Pessoa('C', '3')
p3 = Pessoa('D', '4')
p4 = Pessoa('B', '6')

pessoas = [p1, p2, p3, p4]

print(sorted(pessoas, key=lambda pessoa: pessoa.sobrenome, reverse=False))

print(asdict(p1))  # asdict transforma a classe em um dicionário.
print(astuple(p1))  # astuple transforma a classe em uma tupla.
