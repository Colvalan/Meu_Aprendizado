from datetime import datetime, timedelta

# data = modulo_datetime(2021, 1, 14, 11, 14, 50)  # Dessa maneira, vem formatada por padrão no padrão US.
# print(data.strftime('%d/%m/%y %H:%M:%S'))  # Vamos formatar no padrão brasileiro.
# data = data + timedelta(days=3)
# print(data.strftime('%d/%m/%y %H:%M:%S'))

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:00:00', '%d/%m/%Y %H:%M:%S')
dif = d2 - d1
print(d1 > d2)