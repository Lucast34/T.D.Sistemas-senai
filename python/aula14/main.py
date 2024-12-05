"""
ENCAPSULAMENTO
(Sem underline) = PUBLIC (Pode ser alterado a qualquer momentor)
(Uma underline) =  PROTECTED (Não deve ser alterado fora da classe)
(Dois undelines) = PRIVATE (Não é acessado por outras partes do código)

"""




class Carro:
    def __init__(self,nome,cor,placa,peso,marca):
        self.__nome = nome
        self.cor  = cor 
        self._placa  = placa 
        self.peso  = peso 
        self.marca  = marca 
        self.km_atual = 0

carro1 = Carro('Fiat Uno','Branco','FIATOP',20,'Fiat')

print(carro1) # retona apenas o valor da memoria

# vendo as variaveis

print(vars(carro1))

carro1._placa = 'OI'

print(carro1.__init__)