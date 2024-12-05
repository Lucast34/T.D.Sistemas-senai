"""
Agregação - forma mais especializada de associação 
"""

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def inserirProduto(self,*produtos):
        for p in produtos:
            self.produtos.append(p)

    def listarProdutos(self):
        for produto in self.produtos:
            print(produto.nome)
            print(produto.preco)

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome 
        self.preco = preco

carrinho = Carrinho()

p1 = Produto('Relogio', 350)

p2 = Produto('Hotwheels', 50)

carrinho.inserirProduto(p1,p2)

carrinho.listarProdutos()

print(carrinho.__dict__)