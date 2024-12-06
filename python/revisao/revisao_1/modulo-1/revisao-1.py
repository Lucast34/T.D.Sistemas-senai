'''
Criar uma calculadora com 4 operações
'''
import cauladora as c
try:
    print('-'*5,'Calculadora','-'*5)
    print('> 1-Adição\n> 2-subtração\n> 3-mutiplicação\n> 4-divisão')
    print('Digite >(5)< pra sair')
    operacao = int(input('O que operção que você deseja?\n>>'))
except:
       raise TypeError('\033[0;31m Apenas numero (inteiros) são permitidos\033[m')
else:
    match operacao:
        case 1:
            print('*'*5,'adição','*'*5)
            c.adicao()
        case 2:
            print('*'*5,'subtração','*'*5)
            c.subtracao()
        case 3:
            print('*'*5,'mutiplicação','*'*5)
            c.mutiplicacao()
        case 4:
            print('*'*5,'divisão','*'*5)
            c.divisao()
        case _:
            print('*'*5,'Saindo do programa ;)','*'*5)

# iria ter um finally aqui só que precisaria restruturar todo o código com while
