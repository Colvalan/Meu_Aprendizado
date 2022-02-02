"""
Fizemos um programa que cria uma nova pasta e move ou copia arquivos de uma pasta para
a nova pasta, ou remove arquivos de uma pasta especifica.

No código abaixo, o programa percorre c:\teste 2 e apaga os arquivos contidos nela.
"""

import os
import shutil

caminho_original = r'c:\teste'
caminho_novo = r'c:\teste 2'

try:
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe.')

for raiz, diretorios, arquivos in os.walk(caminho_novo):  # Aqui mudamos para o caminho_novo.
    for arquivo in arquivos:
        caminho_arquivo_antigo = os.path.join(raiz, arquivo)
        caminho_arquivo_novo = os.path.join(caminho_novo, arquivo)

        os.remove(caminho_arquivo_novo)  # Comando usado para excluir os arquivos
        print(f'Arquivo {arquivo} removido com sucesso.')

# NÃO TEM VOLTA APÓS EXECUÇÃO, ARQUIVO É APAGADO PERMANENTEMENTE
