"""
Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele 
acelere o carro e também acrescente algo ao porta malas
"""

class Carro:
    def __init__(self,marca,modelo,cor): # feito
        self._marca = marca # mudado
        self._modelo = modelo # mudado
        self.cor = cor
        self.ligado = False
        self.velocidade = 0
        self.portaMala = 0 

    """
    #@ property <- refatoração
    """
    # Mais objtos
    def ligar(self): # ligando 
        self.ligado = True
        print(f'O carro {self._modelo} etá ligado')

    '''
    Refatoração ligar e desligar ser a mesma coisa
    def motor (self) -> None:
        
        
    '''

    def desligar(self): # desligando
        self.ligado = False
        print(f'O carro {self._modelo} etá desligado')

    def velo(self,km): # Feito
        # adicionando velocidade
        self.velocidade += km
        print(f'O carro está a {self.velocidade}km/h')

    def portaMalapeso(self,kg): # Feito
        # adicionando carga
        self.portaMala += kg
        print(f'O peso do porta mala e de {self.portaMala}kg')

class Motorista:
    def __init__(self,nome,sobrenome,carteira):
        self.nome = nome
        self.sobrenome = sobrenome
        self.carteira = carteira



pessoa = Motorista('Edmar','Gomes','AB')

carro = Carro('Toyota','Trueno-AE86','Branco')

print(pessoa.nome,pessoa.sobrenome,pessoa.carteira)
print(carro._marca,carro._modelo)

carro.ligar()

#adicionando velocida 
carro.velo(90)

carro.desligar()

# adicionando peso 
carro.portaMalapeso(60)


