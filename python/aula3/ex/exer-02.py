numero_multiplo = []

for num in range(1,101):
    print(num,end=' ')
    if num % 10 == 0:
        numero_multiplo.append(num)

print(f'\nMultiplos de 10:{numero_multiplo}')