# Formatando uma data para português.

from datetime import datetime
from locale import setlocale, LC_ALL
from calendar import mdays  # Módulo que usamos para saber qual ultimo dia de cada mes.

setlocale(LC_ALL, 'pt_BR.utf-8')  # Se a string for vazia, usa o idioma do PC do dev.

dt = datetime.now()
mes_atual = int(dt.strftime('%m'))  # Pegamos em numero inteiro, o mês da data.
formatacao1 = dt.strftime('%A, %d de %B de %Y ')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')
print(formatacao1)
print(formatacao2)

# mdays é uma lista, que contém os meses e o ultimo dia de cada um deles onde o index 0 é descartado.

print(mes_atual, mdays[mes_atual])  # Por ser uma lista, usamos o numero do mês como index.

"""
%A = nome do dia.
%d = dia em número.
%B = nome do mês.
%Y = ano 4 digitos.
%y = ano ultimos 2 digitos.
%m = mês em número
%H = hora
%M = minuto
%S = segundo
"""