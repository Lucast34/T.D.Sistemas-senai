'''
faça um algoritmo para calcular a idade da pessoa baseado no ano do seu nascimento
'''

from datetime import datetime as dt

date_nascimento = input('Digite o seu ano de nascimento: ')

data_atual = dt.now().year

print(f'{data_atual - int(date_nascimento)}')