'''
2) João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar um multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um fluxograma que leia a variável P (peso de peixes) e verifique se há excesso. 
Se houver, gravar na variável E (Excesso) e na variável M o valor da multa Que João deverá pagar. 
Caso contrário mostrar tais variáveis com o conteúdo ZERO.
'''

peso_peixe = int(input('Digite o peso: '))

#operador ternario 
response = print(f'Valor da multa:{(peso_peixe - 50) * 4}') if peso_peixe > 50  else print('Sem excesso') 

# antes
# if peso_peixe > 50:
#     peso_excesso = peso_peixe - 50
#     print(f'Valor da multa:{peso_excesso * 4}')
# else:
#     print('Sem excesso')
