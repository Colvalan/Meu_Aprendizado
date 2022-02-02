"""
Fizemos um programa que cria uma nova pasta e move ou copia arquivos de uma pasta para
a nova pasta, ou remove arquivos de uma pasta especifica.

No código abaixo, o programa cria c:\teste 2 e move os arquivos da c:\teste para c:\teste 2
"""

import os
import shutil

caminho_original = r'c:\teste'
caminho_novo = r'c:\teste 1'

# Foi utilizado bloco try porque caso haja uma pasta existente com o mesmo caminho informado
# o programa levantaria execeção FileExistsError.

try:
    os.mkdir(caminho_novo)  # Comando para criar uma nova pasta.
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe.')  # Informa usuário que a pasta já existe

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        caminho_arquivo_antigo = os.path.join(raiz, arquivo)  # Criou uma var com o caminho\nome do arquivo antigo.
        caminho_arquivo_novo = os.path.join(caminho_novo, arquivo) # Criou uma var com o caminho\nome do arquivo novo.

        shutil.move(caminho_arquivo_antigo, caminho_arquivo_novo)  # Comando usado para mover arquivos
        print(f'Arquivo {arquivo} movido com sucesso.')