from modulo_POO.aulas.projeto_ipv4.func import Ip

while True:
    ip = input('Digite um ip válido: ')
    cidr = int(input('Digite um cidr válido: '))

    ip_a_validar = Ip(ip, cidr)
    print(f'Ip: {ip_a_validar.ip}/{ip_a_validar.cidr}')
    print(f'O IP da rede é: {ip_a_validar.rede}/{ip_a_validar.cidr}')
    print(f'O IP de broadcast é: {ip_a_validar.broadcast}/{ip_a_validar.cidr}')
    print(f'O primeiro IP válido é: {ip_a_validar.primeiro_ip}/{ip_a_validar.cidr}')
    print(f'O último IP válido é: {ip_a_validar.ultimo_ip}/{ip_a_validar.cidr}')
    print(f'Máscara de subrede: {ip_a_validar.subrede_decimal}')
    print(f'Total de hosts disponíveis: {ip_a_validar.total_hosts}')
