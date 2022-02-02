import json

with open('abc.json', 'r') as file:  # Abrindo e lendo o modulo_json (dicionário).
    d1_json = file.read()  # criando variavel e passando as chaves e valores do modulo_json para esse novo dicionário.
    d1_json = json.loads(d1_json)  # convertendo esse modulo_json de volta para dicionário

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)

# iteramos o dicionário de maneira que o desempacotamos.
