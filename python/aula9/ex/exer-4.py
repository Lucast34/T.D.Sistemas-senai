'''
Crie um programa que simule um caixa eletrônico. Peça ao usuário um valor a ser sacado e deduza de um saldo inicial. 
Caso o usuário tente sacar mais do que o saldo ou insira um valor inválido, trate o erro de forma apropriada. 
Garanta que o saldo atualizado seja sempre exibido no finally.
'''
def escolha():
    try:
        global conta

        escolha_pri = int(input('curso de seleção >>')) 
    
        match escolha_pri:
            case 1:
                if conta > 10:
                    conta -= 10
                    return conta
               
            case 2:
                if conta > 20:
                    conta -= 20
                    return conta 
                
            case 3:
                if conta > 50:
                    conta -=50
                    #if conta < 0:
                        #raise Exception        
                    return conta 
                else:
                    raise Exception
    except Exception:
        print('SALDO INSUFICIENTE')
            

conta = 45
try:
    print('='*5,'CAIXA ELETRÔNICO','='*5)
    print('1-Retirar dineiro')
    print('2-Sair')

    escolhe = int(input("Escolha um opcão:\n>> "))

    match escolhe:
        case 1:
            print('deseja reitra quanto?')
            print('1 - 10','2 - 20','3-50')
            escolha()
except TypeError:
    print('COMANDO NÃO RECONHECIDO')
finally:
    print(conta)