from zipfile import ZipFile
import os

caminho = r'c:\zip\SC Valdirosh'
with ZipFile('arquivo.zip', 'w') as arquivo_zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        arquivo_zip.write(caminho_completo)