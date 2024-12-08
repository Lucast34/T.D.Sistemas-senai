import miscFunction as m


while True:
    try:
        m.limpar()
        m.menu()

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
            break         
        else:
            print('Ok :)')