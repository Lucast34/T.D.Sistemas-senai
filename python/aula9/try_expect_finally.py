# erros 

# print(10/0) # ZeroDivisionError

# list = [0,1,2,3] #IndexError
# print(list[4])

# dicio = {'chave':'valor'} # KeyError
# print(dicio['VICTOR'])

try:
    NUM_1 = 18
    NUM_2 = 0

    NUM_3 = NUM_1/NUM_2

    list_num = [NUM_3]
    
    raise ZeroDivisionError


except ZeroDivisionError as Error:
    print('NÃO PODE DIVIDIR POR 0')
    print(Error)
except IndexError as Error:
    print('ELEMENTO NA LISTA NÃO EXISTE')
    print(Error)
except KeyError as Error:
    print('DICIONÁRO NÃO EXISTE')
    print(Error)
except Exception:
    print('Algo deu errado')
finally:
    print('Executei')

# TRY - tenta rodar o codigo
# EXECEPT - caso dê um erro especifico 
# FINALLY


# OU
# except:
#     raise ZeroDivisionError('NÃO PODE DIVIDIR POR 0')