import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite um termo: ')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:

        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'KB'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'MB'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'GB'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'TB'
    else:
        tamanho /= peta
        texto = 'PB'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                print(caminho_completo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrado o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho:', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))

            except PermissionError:
                print('Sem permissões')
            except FileNotFoundError:
                print('Arquivo não encontrado')
            except Exception:
                print('Erro desconhecido')

print()
print(f'{conta} arquivo(s) encontrado(s).')
