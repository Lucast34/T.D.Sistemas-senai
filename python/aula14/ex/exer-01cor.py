# W cls
# L ou M clear
from os import system as s 

class Motorista :
    def __init__(self,nome) -> None:
        self.nome = nome
        self.carro = None
        pass

    def associarCarro(self,carro):
        self.carro = carro
        print(f'O motorista {motorista.nome} se associou ao carro!')

class Carro:
    def __init__(self,nome) -> None:
        self.nome = nome
        self.velocidade = 0
        self.portaMalas = ['Step']
    
    def acelerar(self,km) -> None:
        if km <= 0:
            print('Valor invalidado')
        else:
            self.velocidade += km
            print(f'Acelerei {km} km/h')
            print(f'Velocidade atual {self.velocidade}')
       
    
    def adicionarPortaMalas(self,*items) -> None:
        for item in items:
            self.portaMalas.append(item)
        
        for numero,item in enumerate(self.portaMalas):
            print(f'{numero + 1}- {item}')
s('cls')

motorista = Motorista('Victor')
carro = Carro('Lamborguini')

motorista.associarCarro(carro)

motorista.carro.acelerar(100)
motorista.carro.acelerar(60)

motorista.carro.adicionarPortaMalas('compras','Cooler','Mala')

print(motorista.__dict__)

print(vars(carro))