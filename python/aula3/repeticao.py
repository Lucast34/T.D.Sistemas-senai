# condicao = True
 
# while condicao:
#     pergunta= input('Deseja repetir denovo?\n').lower()
#     per_tratado = pergunta.replace('ã','a')

#     if per_tratado == 'nao':
#         break

contador = 1

while contador <= 10:
    print(contador)
    # contador = contador + 1
    contador += 1

    if contador == 5:
        print('Teste')
        continue


    print(contador)