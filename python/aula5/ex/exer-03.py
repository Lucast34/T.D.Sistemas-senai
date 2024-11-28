def media():
    num1 = float(input('Informe a nota:'))*2
    num2 = float(input('Informe a nota:'))*3
    num3 = float(input('Informe a nota:'))*5

    return (num1 + num2 + num3) / (2 + 3 + 5)


print(f'O resulto foi:{media()}')