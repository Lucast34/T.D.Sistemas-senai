num_maior = 0

for i in range(1,4):
    num = int(input(f'Digite o {i}ª número:'))
    
    if num_maior < num:
        num_maior = num

print(f'O número maior foi {num_maior}')