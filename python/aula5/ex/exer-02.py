def imparPar(num):
    response ='é par' if num %2 == 0 else 'não é par'
    return response

numero =  int(input("Digite um numero: "))

print(f'O {numero} {imparPar(numero)}')