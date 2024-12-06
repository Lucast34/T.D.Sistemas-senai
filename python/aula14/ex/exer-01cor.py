class Motorista :
    def __init__(self,nome) -> None:
        self.nome = nome
        self.carro = None
        pass

    def associarCarro(self,carro):
        self.carro = carro
    
class Carro:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.velocidade = 0
        self.portaMalas = ['Step']
        pass


motorista = Motorista('Victor')
carro = Carro('Lamborguini')

motorista.associarCarro(carro)

print(motorista.__dict__)

print(vars(carro))