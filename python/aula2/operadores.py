# operadores logicos

add = 10 + 10 # soma
subt = 10 - 10 #subtrair
multi = 10 * 10 # multiplicar 
divisao = 10 / 10 #divisão
divi_inteira = 10 // 10 # divisão por inteiro 
expo = 10 ** 10 # exponenciação
modulo = 10 % 10 # resto da divisão

# operador relacionais
#> maior 
#< menor 
#>= igual maior
#<= igual menor 
#!= diferente
#== igualdade

# if / else
condicao = True

if condicao:
    print('If')
else:
    print('Else')

# Maior e Menor 
print('-------------------------------------')
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
print('-------------------------------------')

if num1 > num2:
    print('Primeiro número é o maior')
elif num2 > num1:
    print('Segundo número é o maior') 
else:
    print('Ambos são o mesmo número!')