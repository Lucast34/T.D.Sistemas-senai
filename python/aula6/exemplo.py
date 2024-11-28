import os 

usuario = {
    'nome' : 'Victor',
    'email' : 'emailtop@gmail.com',
    'senha' : '!1234',
    'cpf' : 9999999,
    'vip': True,
    'endereco' : [
        {
            'rua' : 13,
            'cidade' : 'Ceilândia',
            'estado' : 'DF'
        }
    ]
}

# print(usuario['nome'])

# print(usuario, type(usuario))

# pesquisa = input("digite o que quer achar:")

# print(usuario[pesquisa])

#Metodo

# len - Vê quantas chaves tem no dicionario
# keys - Retorna chaves
# values - Retorna valores 
# items - Retona chaves e valores
# setdefault - Adciona valor se a chave não existe
# get - busca a chave 
# pop - apaga uma chave específica 
# popitem - apaga a ultima chave 
# update - atualiza uma chave


os.system('cls')

print(len(usuario))

print(tuple(usuario.keys()))

print(list(usuario.values()))

print(list(usuario.items()))

usuario.setdefault('saldo', 1.255)

print(usuario)

print(usuario.get('nome'))

usuario.pop('nome')

print(usuario)

usuario.popitem()
print(usuario)

usuario.update({
    'nome': 'Victor',
    'email': 'victor.ro@yahoo.com'
})

print(usuario)