ValorTotal = 0

def somarValor(ValorProduto):
    global ValorTotal

    #ValorProduto = float(input('PRECO DO PRODUTO:'))
    ValorTotal += ValorProduto


somarValor(30)
somarValor(5)
somarValor(47)

print(f'valor total é de R$:{ValorTotal}')