import miscFunction as m
import random

# (^-^)
while True:
    ex = 0
    try:
        m.limpar()
        m.menu()

        ex += 1
        m.emot() if ex > 5 else ''

        print('Escolha uma opção')
        escolha = int(input('>> '))
        
        match escolha:
            case 1:
                print('test00')
            case 2:
                print('test01')
    


    except error:
        if error == ValueError :
            print('algo deu errado quer tentar novamente?')  

    finally:
        print("Deseja sair do programa(s/n)")
        escolha_dnv = input(">> ").lower()
        
        if escolha == 's':
            print('(^-^)')
            break         
        else:
            print('Ok :)')