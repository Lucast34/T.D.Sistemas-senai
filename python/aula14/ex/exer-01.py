"""
Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele 
acelere o carro e também acrescente algo ao porta malas
"""

class Carro:
    def __init__(self,marca,modelo,cor) -> None:
        self.__marca = marca
        self.__modelo = modelo
        self.cor = cor
        self.velocidade = 0
        self.portaMala = 0 
    
    def velo(self,km) -> None:
        self.velocidade += km
        print(f'O carro está a {self.velocidade}km/h')

    def portaMalapeso(self,kg) -> None:
        self.portaMala += kg
        print(f'O peso do porta mala e de {self.portaMala}kg')

carro = Carro('Toyota','Trueno-AE86','Branco')

print(carro.marca,carro.modelo)

carro.portaMalapeso(60)

carro.velo(90)