#maça, laranja ou banana
print('---------------------------------')
print('menu')
print('---------------------------------')
print('1 - maçã')
print('2 - banana')
print('3 - uva')
produto = int(input('qual fruta deseja comprar? '))
qtd = int(input('quantas? '))

match (produto):
    case 1: 
        produto == 1
        pagar = qtd * 2.3
        print(f'você comprou {qtd}! total a pagar: {pagar}')
    case 2:
        produto == 2
        pagar = qtd * 4.5
        print(f'você comprou {qtd}! total a pagar: {pagar}')
    case 3:
        produto == 3
        pagar = qtd * 3.5
        print(f'você comprou {qtd}! total a pagar: {pagar}')
    case _:
        print('produto inexistente')



