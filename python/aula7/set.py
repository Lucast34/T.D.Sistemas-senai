'''
Sets - conjunto

1º Não tem indice ou seja não garante ordem 
2º Não aceita conteudo repetido
'''

# a = set('Levy')

# test = ['OI', 'OI', 'OI']

# print(a)

# print(test)
# print(set(test))

# b = {'Victor',1, 2, 3, 4, 5, 6}

# print(b)
# print(type(b))

# c = set()

# print(type(c),c)


#Metodos uteis
# conjunto = set()

# conjunto.add(10)
# conjunto.add(8)

# conjunto.update((3,5,6,'BOM DIA'))

# print(f'Print do update: {conjunto}')

# conjunto.discard('BOM DIA')

# print('*'*10)
# print(conjunto)

# uniâo (union) - une dois
# interseção (intersection) -  junta apenas o item comum nos dois
# diferença - item presente apenas em um

conjunto_a = {1,2,3,4,5}
conjunto_b = {5,6,7,8,9}

conjunto_c = set()
# | union
conjunto_c = conjunto_a | conjunto_b
# & intersection
##conjunto_c = conjunto_a & conjunto_b
# - diference
##conjunto_c_di =  conjunto_a - conjunto_b
##conjunto_c_di_b =  conjunto_b - conjunto_a
# ^ diference = diferença em relação a ambos os conjuntos
##conjunto_c_d = conjunto_a ^ conjunto_b

print(conjunto_c)

#print(conjunto_c_di)

#print(conjunto_c_di_b)

# set é interavel
for i in conjunto_c:
    print(i)