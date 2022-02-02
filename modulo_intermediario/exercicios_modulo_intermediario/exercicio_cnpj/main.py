from funcoes_cnpj import cnpj_format, convert_list_int,\
    primeiro_digito, segundo_digito, convert_list_str_full, validador

while True:
    cnpj = cnpj_format(input('Digite o CNPJ a ser validado: '))  # CNPJ sairá formatado.

    # Tratando dados contra trolagem do usuário.

    if not cnpj.isdigit():
        print('Digite apenas numeros.')
        continue
    elif cnpj == cnpj[0] * len(cnpj):
        print('Sequencias não são válidas')
        continue

    cnpj_a_validar = convert_list_int(cnpj)  # Converti o cnpj em uma lista de inteiros excluindo os 2 ultimos digitos.
    mult_digito1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # Multiplicadores do primeiro digito conforme algorítmo.

    # Função 'primeiro_digito' vai fazer todos os calculos necessários para verificar o digito 1.
    digito1 = primeiro_digito(cnpj_a_validar, mult_digito1, 0, 0)
    cnpj_a_validar.append(digito1)  # Adicionei o primeiro digito ao cnpj a ser validado.
    mult_digito2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]  # Multiplicadores do segundo digito conforme algorítmo.

    # Função 'segundo_digito' vai fazer todos os calculos necessários para verificar o digito 2.
    digito2 = segundo_digito(cnpj_a_validar, mult_digito2, 0, 0)
    cnpj_a_validar.append(digito2)  # Adiciono o digito 2 ao cnpj a ser verificado.
    cnpj_a_validar = convert_list_str_full(cnpj_a_validar)  # Converto o cnpj a ser verificado em uma string.

    # Função validador valida se o cnpj a ser verificado é igual ao cnpj original.
    checando_cnpj = validador(cnpj_a_validar, cnpj)
    print(checando_cnpj)  # Informo ao usuário se o cnpj é válido ou inválido.
