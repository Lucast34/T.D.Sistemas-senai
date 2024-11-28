'''
1. Cadastro de Produto
Você precisa criar um programa que armazene informações de um produto em um dicionário. 
As informações devem incluir nome, preço e quantidade em estoque. 
Depois, o programa deve exibir todas as informações do produto.
'''

produto_dicio = {
    'nome':['Leite','Pastel'],
    'preco': [8.60,4.99],
    'estoque': [5,15]
}

# print(produto_dicio.values)

nome = input('Nome do produto:\n>>')
produto_dicio.get('nomes').append(nome)

preco = float(input('Preço do produto:\n>>'))
produto_dicio.get('Preco').append(preco)

estoque = int(input('Quantidade de estoque:\n>>'))
produto_dicio.get('Estoque').append(estoque)

for produto in produto_dicio.item():
    print(f'{produto[0]}')
    print(f'{produto[1]}')

