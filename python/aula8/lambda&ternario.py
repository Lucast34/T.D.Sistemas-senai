def conveterDolar(valor):
    valor *= 5.82
    return valor

print(conveterDolar(5))

# lambada é basicamenete um def ternario <- Ou seja só operações simples 
# ajuda na legibilidade 
conveterEuro = lambda valor : valor * 6.66
conveterIene = lambda valor  , taxa : valor / 0.03 - taxa

print(conveterEuro(5))
print(conveterIene(1000,40))

# ternario
condicao = False

print('if') if condicao else print('else')

valor = 0
valor = 1  if condicao else valor

print(valor)