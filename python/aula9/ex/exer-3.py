'''
Solicite ao usuário que insira seu peso e altura. 
Calcule o IMC, mas trate possíveis erros, como entradas inválidas ou divisões por zero. 
Garanta que o programa sempre informe o status do processo no finall
'''
try:
    peso = float(input('Digite o seu peso:\n>> '))
    altura = float(input('Digite a sua altura:\n>> '))

    IMC = peso / altura ** 2

    print(f'O seu imc:{IMC:.2f}')
except ZeroDivisionError as error:
    print(f"{error}\nA altura não pode ser 0")