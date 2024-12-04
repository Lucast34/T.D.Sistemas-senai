import json as j



def cadastro():
    unome= input('Digite o seu nome >>')
    user = input('Digite o seu login >>')
    ucpf = int(input('Digite o seu cpf >>'))
    

    while True:
        usenha = input('Digite o seu senha >>')
        c_usenha= input('Confirme a sua senha >>')

        if usenha == c_usenha:
            break
        else:
            print('Senha não são iguais tente novamente!')

    usuario_dicio = {
        'nome':unome,
        'user': user,
        'cpf': ucpf,
        'senha': usenha
    }


    with open('python/aula12/ex/correcao/dados.json','w',encoding='utf8') as leitura:
        j.dump(
            usuario_dicio,
            leitura,
            indent= 2
        )
