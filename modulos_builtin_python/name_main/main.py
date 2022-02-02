"""
Aula sobre __name__ == __main__

Isso serve para definir, que uma parte do código só rode, se o arquivo em que ele se encontra
esteja sendo rodado diretamente.

- Se um arquivo é executado diretamente, tem seu nome como __main__.

- Se um arquivo é executado através de uma importação, por outro arquivo
ele tem seu nome como o nome real do arquivo. Nesse exemplo, terá o nome de modulo.

Para isso, usamos if __name__ == '__main__'
"""

from modulos_builtin_python.name_main.modulo import soma

# Note que se não constar o if __name__ == '__main__' no arquivo modulo, será executado
# o teste que fiz no outro arquivo.

soma(1, 4)

