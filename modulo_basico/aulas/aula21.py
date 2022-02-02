# Índices
# 0123456789.................33

# Esse exemplo vai criar uma nova string a partir de uma string pré configurada.
# Nossa string nesse caso sera "Em 2022 serei programador python com a graça de Deus."
# Será criada uma variável contendo também o comprimento da string

frase = 'Em 2022 serei programador python com a graça de Deus.'
tamanho_frase = len(frase)

# Será criado um contador para a funcão while funcionar.

contador = 0

# Nossa nova string começa vazia

nova_string = ''

# Será criada uma variável para que o usuário informe se ele quer alguma letra maiúscula

input_do_usuario = input('Qual letra deseja formatar para maiúsculo?: ')

# Aqui começa a função while para montar a nova string.

while contador < tamanho_frase:  # Enquanto contador for menor que o tamanho da frase
    letra = frase[contador]  # Letra será uma das letras de nossa string de acordo com índice informado
    if letra == input_do_usuario:  # Se a variavel letra for == á input do usuário
        nova_string = nova_string + input_do_usuario.upper()  # Vamos adicioná-la a nossa nova string como maiúscula
    else:
        nova_string = nova_string + letra  # Se não, adiciona a letra a nossa nova string
    contador = contador + 1  # Somamos 1 ao nosso contador. Quando ele for < que o tamanho da frase, encerra o laço.

print(nova_string)   # imprime nossa nova string.

# Lógica um pouco mais complexa, mas comentando bem, da para entender numa boa!
