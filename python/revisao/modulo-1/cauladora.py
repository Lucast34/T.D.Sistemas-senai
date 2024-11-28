# Fuções da calculadora o nome foi uma piadinha muito interna 
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

