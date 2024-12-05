"""
Agregação - forma mais especializada de associação 
"""

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def inserirProdutos(self,produto):
        self,produto.append(produto)

class Produtos:
    def __init__(self,nome,preco):
        self.nome = nome 
        self.preco = preco

carrinho = Carrinho()
p1 = Produtos('Relogio', 350)