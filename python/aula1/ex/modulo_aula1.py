'''
Escreva um algoritimo que leia nome, email e senha de um usuario e mostre apos o cadastro os dados salvos
'''

def dicio():
    NOME = input("Digite o seu nome:\n>>")
    EMAIL = input("Digite o seu email:\n>>")
    SENHA = input("Senha:\n>>")

    pessoa={
        'nome':NOME,
        'email':EMAIL,
        'senha':SENHA
    }

    print(f'Cadastro realizado com sucesso:\n- Nome:{pessoa["nome"]}\n- E-mail:{pessoa["email"]}\n- Senha:{pessoa["senha"]}')


'''
faça um algoritmo para calcular a idade da pessoa baseado no ano do seu nascimento
'''

from datetime import datetime as dt

def calc_nasc():
    date_nascimento = input('Digite o seu ano de nascimento: ')

    data_atual = dt.now().year

    print(f'{data_atual - int(date_nascimento)}')