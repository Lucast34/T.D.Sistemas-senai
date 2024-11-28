NOME_USUARIO = 'Lorena'
SENHA_USUARIO = '1234'

nome = input('Digite o seu nome: ')
senha = input('Digite o seu senha: ')

# if NOME_USUARIO == nome and SENHA_USUARIO == senha:
#     print('Acesso autorizado')
# else:
#     print('Acesso negado')

# if NOME_USUARIO == nome or SENHA_USUARIO == senha:
#     print('Acesso autorizado')
# else:
#     print('Acesso negado')

if not NOME_USUARIO == nome and not SENHA_USUARIO == senha:
    print('Acesso autorizado')
else:
    print('Acesso negado')