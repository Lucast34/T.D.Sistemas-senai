import miscFunction as m


while True:
    try:
        m.limpar()
        m.menu()

        escolha = int(input('Escolha uma opeção'))
        
        match escolha:
            case 1:
                print('test00')
            case 2:
                print('test01')
    


    except error:
        if error == ValueError :
            print('algo deu errado quer tentar novamente?')  

    finally:
        print("Deseja continuar no programa(s/n)").lower()
        escolha_dnv = int(input(">> "))

         