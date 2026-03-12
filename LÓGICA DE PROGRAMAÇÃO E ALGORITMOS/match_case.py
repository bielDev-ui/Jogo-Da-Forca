def checagem_tipo(dado):
    match dado:
        case str(dado):
            print("String:", dado)
        case int(dado):
            print("Inteiro:", dado)
        case float(dado):
            print("Float:", dado)
        case _:
            print('tipo de dado descohecido')

dados = ['JAKE', 30, 3.87, 'VALENTIN']

for dado in dados:
    checagem_tipo(dado)