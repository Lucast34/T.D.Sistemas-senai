import json as j

def login():
    user = input('Digite o seu login >>')
    usenha = input('Digite o seu senha >>')

    json_path = 'python/aula12/ex/correcao/dados.json'

    with open(json_path,'r',encoding='utf8') as leitura:
        dados = j.load(leitura)
        c_usuario = dados['user']
        c_senha = dados['senha']
        c_nome = dados['nome']

    if c_usuario == user and c_senha == usenha:
        print(f'Seja bem-vindo(a),{c_nome}')
    else:
        print('A senha ou usuario estão incorretos, tente novamente')
    