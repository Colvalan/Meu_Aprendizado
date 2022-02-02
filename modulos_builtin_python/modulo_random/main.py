import random
import string

# Gera um numero inteiro entre X e Y
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um numero de ponto flutuante entre X e Y
flutuante = random.uniform(10, 20)

# Gera um numero de ponto flutuante entre 0 e 1
flutuante_1 = random.random()


lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']
sorteio = random.choice(lista)  # Sorteia 1 indice na lista.
sorteio_1 = random.choices(lista, k=2)  # Sorteia varios indices de uma lista conforme assinatura. Pode repetir.
sorteio_2 = random.sample(lista, 2)  # Sorteia varios indices de uma lista mas sem repetição.

# Se quiser embaralhar uma lista, usamos o seguinte.
random.shuffle(lista)

# Gera senha aleatória
letras = string.ascii_letters
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(f'{flutuante_1:.2f}')
