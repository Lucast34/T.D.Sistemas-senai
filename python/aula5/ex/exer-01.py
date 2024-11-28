# def mutiplicador(num1, num2, num3):
#     total = num1 * num2 * num3
#     return total

# print(f'O valor total mutiplicado é {mutiplicador(5,5,5)}') 


def operacao(*numeros):
    resultado = 1

    for numero in numeros:
        resultado *= numero
        print(f'O valor total da operação de: {resultado}')

operacao(2,2)
