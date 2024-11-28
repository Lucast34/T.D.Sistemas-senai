'''
Faça um algoritmo que avalie se o usuario e senha cadastrados e 
se não tiver, printe uma falha
senao printe que deu tudo certo
(considerar que usuario e senha sejam ''ADM')
'''



def usuario():
    senha = '1234'
    usuario = 'SenaiADM'
    
    usuario_insert = input('Digite o usuario:\n>>') 
    senha_insert = input('Digite senha:\n>>') 
    
    response =  'Conta logado, Bem vindo' if senha_insert == senha and usuario  == usuario_insert else 'FALHA '

    return response

print(usuario())