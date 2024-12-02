'''
Escreva um algoritimo que leia nome, email e senha de um usuario e mostre apos o cadastro os dados salvos
'''

def dicio():
    NOME = input("Digite o seu nome: ")
    EMAIL = input("Digite o seu email: ")
    SENHA = input("Senha: ")

    pessoa={
        'nome':NOME,
        'email':EMAIL,
        'senha':SENHA
    }

    print(f'Cadastro realizado com sucesso:\n- Nome:{pessoa["nome"]}\n- E-mail:{pessoa["email"]}\n- Senha:{pessoa["senha"]}')