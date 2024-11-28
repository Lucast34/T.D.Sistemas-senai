'''
Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).
'''

#fazendo de todas as tabuadas

def tabuada(num_ins):
    # lambda
    # tabuada = [(lambda num : num * num_ins) (num) for num in range(1,11)]

    # parte do lambda 
    # return print (f'{tabuada}')

    # so com list compreension  
    tabuada = [print(f'{num_ins} * {num} = {num * num_ins}') for num in range(1,11)]
    
    # parte do list compreension
    return tabuada


num_ins = int(input("Digite um nuemero:"))

tabuada(num_ins)