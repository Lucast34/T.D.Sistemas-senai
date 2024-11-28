'''
1. Cadastro de Produto
Você precisa criar um programa que armazene informações de um produto em um dicionário. 
As informações devem incluir nome, preço e quantidade em estoque. 
Depois, o programa deve exibir todas as informações do produto.
'''

produto_dicio = {
    'nome':'Leite',
    'preco': 14.60,
    'estoque': 5
}


print(f'>Nome:{produto_dicio['nome']}\n>Preco:{produto_dicio['preco']}\n>Estoque:{produto_dicio['estoque']}')
