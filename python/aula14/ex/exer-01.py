"""
Crie um class motorista e um class carro, associe o carro ao motorista e possibilite que ele 
acelere o carro e também acrescente algo ao porta malas
"""

class Carro:
    def __init__(self,marca,modelo,cor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.portaMala = 0 

    def PortaMala(self) -> None:
        pass