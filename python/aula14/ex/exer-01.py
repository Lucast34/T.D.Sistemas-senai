"""
Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele 
acelere o carro e também acrescente algo ao porta malas
"""

class Carro:
    def __init__(self,marca,modelo,cor) -> None: # remover None
        self.__marca = marca # private <- acho melhor trocar pro protected 
        self.__modelo = modelo # private <- acho melhor trocar pro protected
        self.cor = cor
        self.velocidade = 0
        self.portaMala = 0 

    """
    #@ propeerty <- refatoração
    """
    
    def velo(self,km) -> None:  # remover None
        # adicionando velocidade
        self.velocidade += km
        print(f'O carro está a {self.velocidade}km/h')

    def portaMalapeso(self,kg) -> None: # remover None
        # adicionando carga
        self.portaMala += kg
        print(f'O peso do porta mala e de {self.portaMala}kg')

carro = Carro('Toyota','Trueno-AE86','Branco')

print(carro.marca,carro.modelo)

# adicionando peso 
carro.portaMalapeso(60)

#adicionando velocida 
carro.velo(90)
