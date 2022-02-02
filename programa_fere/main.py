from openpyxl import load_workbook
import os

workbook = load_workbook('Template.xlsx')

planilha = workbook.active

produtos = [
    [0, 'Argamassa', 100],
    [1, 'Cimento', 50],
    [2, 'Cola', 20],
    [3, 'Reboco', 100]
]

num_pedido = input('Digite o número do pedido: ')
print()
produto1 = int(input('Código do produto 1: '))
planilha['A2'] = produto1
planilha['B2'] = produtos[produto1][1]
print()
qtd_produto1 = int(input('Quantidade do produto 1: '))
planilha['C2'] = qtd_produto1
planilha['D2'] = produtos[produto1][2]
planilha['E2'] = produtos[produto1][2] * qtd_produto1

print()
continuar1 = input('Deseja adicionar segundo item ao pedido?\n"s" para Sim, "n" para Não: ')

if continuar1 == 's':

    print()
    produto2 = int(input('Código do produto 2: '))
    planilha['A3'] = produto2
    planilha['B3'] = produtos[produto2][1]
    print()
    qtd_produto2 = int(input('Quantidade do produto 2: '))
    planilha['C3'] = qtd_produto2
    planilha['D3'] = produtos[produto2][2]
    planilha['E3'] = produtos[produto2][2] * qtd_produto2

    print()
    continuar2 = input('Deseja adicionar terceiro item ao pedido?\n"s" para Sim, "n" para Não: ')

    if continuar2 == 's':

        print()
        produto3 = int(input('Código do produto 3: '))
        planilha['A4'] = produto3
        planilha['B4'] = produtos[produto3][1]
        print()
        qtd_produto3 = int(input('Quantidade do produto 3: '))
        planilha['C4'] = qtd_produto3
        planilha['D4'] = produtos[produto3][2]
        planilha['E4'] = produtos[produto3][2] * qtd_produto3

        print()
        continuar3 = input('Deseja adicionar quarto item ao pedido?\n"s" para Sim, "n" para Não: ')

        if continuar3 == 's':

            print()
            produto4 = int(input('Código do produto 4: '))
            planilha['A5'] = produto4
            planilha['B5'] = produtos[produto4][1]
            print()
            qtd_produto4 = int(input('Quantidade do produto 3: '))
            planilha['C5'] = qtd_produto4
            planilha['D5'] = produtos[produto4][2]
            planilha['E5'] = produtos[produto4][2] * qtd_produto4

print()
workbook.save(filename=f"{num_pedido}.xlsx")
os.startfile(f"{num_pedido}.xlsx", "print")
print('Pedido salvo com sucesso.')
