import login as l
import cadastro as c

while True:
    try:
        print('1 - cadastro\n2 - login')
        option = input('O que deseja fazer?\n>> ')

        match option:
            case'1':
                c.cadastro()
            case '2':
                l.login()
    except ValueError:
        print('Valor invalido')
    except Exception:
        print('Algo deu errado :/')