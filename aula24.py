from vendas.calc_preco import aumento, reducao

# Do vendas, modulo calc_preco, importe as funções aumento e reducao

preco = 49.90
preco_com_aumento = aumento(preco, 15, formata=True)
preco_com_reducao = reducao(preco, 15, formata=True)
print(preco_com_aumento)
print(preco_com_reducao)
