'''
Aplicação que pegue o número de clientes em uma mesa, 
o valor total da conta e após isso divida a conta de forma igual a todos os clientes
'''
# OMG list HIIIIIIIII
dinhe_List = []

pessoa = int(input('teste:\n>>'))

# Repetição 
for i in range(pessoa):
    dinheiro = int(input(f'Conta da {i+1}º pessoa: '))
    dinhe_List.append(dinheiro)

#Creio que tem outra forma de fazer isso ZZZZZZZZZ

print(f'A conta deu :\n{sum(dinhe_List)/pessoa}')
