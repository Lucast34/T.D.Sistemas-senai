def media():
    num1 = float(input('Informe a nota:'))*2
    num2 = float(input('Informe a nota:'))*3
    num3 = float(input('Informe a nota:'))*5
    num4 = float(input('Informe a nota:'))*1

    result = (num1 + num2 + num3 + num4) / (2 + 3 + 5 + 1)

    reponse = f'Passou com a nota {result:.2f}'if result > 7 else f'Não passou, Nota: {result:.2f}'
    return reponse 

print(f'{media()}')