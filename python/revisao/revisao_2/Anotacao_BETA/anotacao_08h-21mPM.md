# Documentação

Decidir documentar o processo de "BETA" dos meu codigos tanto para agilizar raciocinos e para comparar meu progresso no futuro.
E melhorar minha digitação e gramatica.

## Historico de commits

> commit 1:

1 - classe sendo declarada, atributos e etc

``` python
classe declarada:
            class Estoque:
                def __init__(self,produto)-> None:    # < - a classe principal precisa compilar tudo aqui e mandar no dicionario 
                    self.produto = produto
                    self.quantida = quantidade 
```

O `def __init__` é uma estrutura que monta a classe. O que vai ter nela, quais os atributos ela vai ter podendo até mesmo ser vazia.
Por exemplo eu poderia deixar essa parte:

``` python
# Antes 
self.produto = produto
self.quantida = quantidade

# Depois
self.produto = str
self.quantidade = int 
```

como o `__init__` é um construtor ela tem que vir primeiro junto com o parânmentro `(self)`.
O `self` é uma forma da classe chamar si mesma.

```  python
# O código inteiro:
while True:     #<---- Repetir infinitamente


        try: #<--- Tratamente de erro
            class Estoque:
                def __init__(self,produto)-> None:  # < - a classe principal 
                    self.produto = produto
                    self.quantida = quantidade 
                #precisa compilar tudo aqui e mandar no dicionario 

            @propety:
                def EstoqueAdd(self):
                    quantida += quantidade
            class Produto:
                def __init__ (self) -> None:
                    pass 
        except Exception: #<-- Se der erro 
            print('Sei la que deu nesssa porra fica quieto ai')
            break
```
