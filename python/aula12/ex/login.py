import miscFunction as m
import random

ex = 0

# (^-^)
while True:
    try:
        
        m.limpar()
        m.menu()

        ex += 1
        
        print(m.emot() if ex > 5 else '')

        print('Escolha uma opção')
        escolha = int(input('>> '))
        
        match escolha:
            case 1:
                print('test00')
            case 2:
                print('test01')
    


    except ValueError:
            print('algo deu errado quer tentar novamente?')  

    finally:
        print("Deseja sair do programa(s/n)")
        escolha_dnv = input(">> ").lower()
        