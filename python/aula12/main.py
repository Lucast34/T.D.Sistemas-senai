arquivo = 'main.txt'

# W / escrita
# R / read
# X / criação
# T / modo texto
# W+, R+ / escrita e leitura
# b / binario

# leitura = open(arquivo,'w')
    #codigo aqui
# leitura.close()

#metodo 2 

with open(arquivo,'w+') as leitura:
    # write - escreva uma linha
    # writelines - escreva mutiplas linhas
    # seek - move cursor

    leitura.write('test\n')
    leitura.write('test2\n')
    leitura.seek(0,0)
    leitura.writelines(
        'test3\n','test4\n'
        )
    

with open(arquivo,'w+') as leitura:
    print(leitura.read())
    print(leitura.readline().strip())



print(type(leitura))

print(arquivo)
