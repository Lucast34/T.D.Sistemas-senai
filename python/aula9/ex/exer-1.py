# fazer com lambda e ternario

def adicao():
    num = int(input('Digite o 1º numero:\n>>'))
    num2 = int(input('Digite o 2º numero:\n>>'))

    print(f'Resultado:\n{num}+{num2}={num + num2}')

def subtracao():
    num = int(input('Digite o 1º numero:\n>>'))
    num2 = int(input('Digite o 2º numero:\n>>'))

    print(f'Resultado:\n{num}+{num2}={num - num2}')

def mutiplicacao():
    num = int(input('Digite o 1º numero:\n>>'))
    num2 = int(input('Digite o 2º numero:\n>>'))

    print(f'Resultado:\n{num}+{num2}={num * num2}')

def divisao():
    try:
        num = int(input('Digite o dividendo:\n>>'))
        num2 = int(input('Digite o divisor:\n>>'))
    except ZeroDivisionError:
        return 0
    else:
        print(f'Resultado:\n{num}+{num2}={num / num2}')


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
            adicao()
        case 2:
            print('*'*5,'subtração','*'*5)
            subtracao()
        case 3:
            print('*'*5,'mutiplicação','*'*5)
            mutiplicacao()
        case 4:
            print('*'*5,'divisão','*'*5)
            divisao()
        case _:
            print('*'*5,'Saindo do programa ;)','*'*5)