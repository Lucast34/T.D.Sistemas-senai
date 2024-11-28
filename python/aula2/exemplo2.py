
print('===================================================')
print('A) PAMONHA - R$7,00')
print('B) CALDO - R$4,00')
print('C) PASTEL - R$6,99')
print('D) CAFÉ - R$3,00')
print('E) CANCELAR')
print('F) COMPRAR')
print('===================================================')

opcao = input('Seleciano o que deseja comprar: ').lower()
valorTotal = float
lojinha = 'sim'

while lojinha == 'sim':
    match opcao:
        case 'a':
            print('Item adicionado')
            #valorTotal = 7.00 
        case 'b':
            print('Item adicionado')
            #valorTotal += 4.00 
        case 'c':
            print('Item adicionado')
            #valorTotal = 6.99 
        case 'd':
            print('Item adicionado')
            #valorTotal = 3.00 
        case 'e':
            print('Cancelado!')
        case 'f':
            print('Total de pedido: ', valorTotal)

    adicionar = input('Deseja adcionar algo?\n').lower()

    #adicionar.replace('ã','a')
