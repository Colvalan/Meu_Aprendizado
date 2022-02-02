

# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as error:  # Aqui, geramos um log do erro.
#         print('Log: ', error)
#         raise  # Raise, permite que a excecão seja capturada fora dessa função
#
#
# try:
#     print(divide(2, 0))
# except ZeroDivisionError as error:  # Devido uso do Raise na função, capturamos a mesma também fora da função.
#     print(error)

# Lançando minhas própria exceções.


def divide(n1, n2):
    if n2 == 0:  # O nome da exceção usada será 'ValueError'.
        raise ValueError("n2 não pode ser 0.")  # uso raise pra que a exceção seja capturada fora da função
    return n1 / n2


try:
    print(divide(2, 0))
except ValueError as error:  # Devido uso do raise, aqui a exceção será capturada normalmente
    print('Não pode dividir por 0!')  # Mensagem explicando ao usuário qual o problema.
    # print(error)
