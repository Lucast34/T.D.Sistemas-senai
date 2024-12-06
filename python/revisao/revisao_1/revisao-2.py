'''
Programe um algoritmo onde podemos colocar um valor em reais e logo a pós perguntar qual moeda deseja converter 
( Dólares, Ienes ou euro) e logo após isso fazermos a conversão 
'''

# funções
def menu():
    while True:    
            try:
                print('Qual moeda você deseja converter.')
                print('-> 1 Dolar\n-> 2 Ienes\n-> 3 Euro')

                escolha = int(input('ESCOLHA:\n>>'))

                valor = float(input('Quanto deseja converter'))

                match escolha:
                    case 1:
                        print('Dolar')
                        print(f'A conversão de dolar e de {(valor/5.81):.1f}')
                    case 2:
                        print('Iene')
                        print(f'A conversão de dolar e de {(valor/ 0.03):.1f}')
                    case 3:
                        print('Euro')
                        print(f'A conversão de dolar e de {(valor/ 6.05):.1f}')
                    case -1:
                        break
            except TypeError:
                return 0
            finally:
                return escolha
            

print('-'*5,'Conversão de moedas','-'*5)

print(menu())