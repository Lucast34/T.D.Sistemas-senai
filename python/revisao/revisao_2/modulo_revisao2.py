import os
# ᓀ‸ᓂ 

def apagar():
    if os.plataform() == 'win32':
        os.system('cls')
    else:
        os.system ('clear')




def ex1():
    dicio = { 
        'produto' : 'nome_produto',
        'quantidade' : 'quantidade_estoque',
        'preco':'preco_lol'
        }

    while True:
    
        try:
            class Estoque:
                def __init__(self,produto, quantidade)-> None:    # < - a classe principal precisa compilar tudo aqui e mandar no dicionario 
                    self.produto = produto
                    self.quantida = quantidade 
            
            
            @property 
            def EstoqueAdd(self):
                ...

            @setter
            def EstoqueAdd(self):

            class Produto:
                def __init__ (self) -> None:
                    self.nome : nome


            class AddProduto:

                
        except Exception:
            print('Sei la que deu nesssa porra fica quieto ai')
            break


def ex2():
    class Pedido:
        def __init__(self) -> None:
            ...
    
    class ItemPedido:
        def __init__(self) -> None:
            ...
    
    class Cardapio:
        def __init__ (self) -> None:
            ...
    ...

def ex3():
    ...

def ex4():
    ...
    