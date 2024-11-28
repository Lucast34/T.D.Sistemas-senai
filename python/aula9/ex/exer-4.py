'''
Crie um programa que simule um caixa eletrônico. Peça ao usuário um valor a ser sacado e deduza de um saldo inicial. 
Caso o usuário tente sacar mais do que o saldo ou insira um valor inválido, trate o erro de forma apropriada. 
Garanta que o saldo atualizado seja sempre exibido no finally.
'''

conta = 45

print('='*5,'CAIXA ELETRÔNICO','='*5)
print('1-Retirar dineiro')
print('2-Sair')

escolhe = int(input("Escolha um opcão:\n>> "))

match escolhe:
    case 1:
        print(deseja reitra quanto?)
        print()

print(conta)