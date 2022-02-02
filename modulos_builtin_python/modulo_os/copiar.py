"""
Fizemos um programa que cria uma nova pasta e move ou copia arquivos de uma pasta para
a nova pasta, ou remove arquivos de uma pasta especifica.

No código abaixo, o programa cria c:\teste 2 e copia os arquivos da c:\teste para c:\teste 2
"""

import os
import shutil

caminho_original = r'c:\teste'
caminho_novo = r'c:\teste 2'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe.')

for raiz, diretorios, arquivos in os.walk(caminho_original):
    for arquivo in arquivos:
        caminho_arquivo_antigo = os.path.join(raiz, arquivo)
        caminho_arquivo_novo = os.path.join(caminho_novo, arquivo)

        shutil.copy(caminho_arquivo_antigo, caminho_arquivo_novo)  # Copiou os arquivos do caminho antigo para o novo.
        print(f'Arquivo {arquivo} movido com sucesso.')