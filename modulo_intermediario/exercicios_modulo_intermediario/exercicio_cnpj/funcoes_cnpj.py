def cnpj_format(cnpj):
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def convert_list_int(cnpj):
    lista = [int(x) for x in cnpj]
    return lista[0: 12]


def convert_list_str_full(cnpj_a_validar):
    lista = ''.join([str(x) for x in cnpj_a_validar])
    return lista


def primeiro_digito(cnpj_a_validar, mult_digito1, index_mult_digito1, resultado_digito1):
    for v in cnpj_a_validar:
        v = v * mult_digito1[index_mult_digito1]
        index_mult_digito1 += 1
        resultado_digito1 += v
    conta = 11 - (resultado_digito1 % 11)
    if conta > 9:
        return 0
    else:
        return conta


def segundo_digito(cnpj_a_validar, mult_digito2, index_mult_digito2, resultado_digito2):
    for v in cnpj_a_validar:
        v = v * mult_digito2[index_mult_digito2]
        index_mult_digito2 += 1
        resultado_digito2 += v
    conta = 11 - (resultado_digito2 % 11)
    if conta > 9:
        return 0
    else:
        return conta


def validador(cnpj_a_validar, cnpj):
    if cnpj_a_validar == cnpj:
        return 'CNPJ Válido'
    else:
        return 'CNPJ Inválido'
