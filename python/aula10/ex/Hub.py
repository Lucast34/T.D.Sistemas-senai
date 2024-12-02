import mEx as m
import os

while True:
    m.menu()
    try:
        escolha = int(input('Escolha um do exercicios:\n>> '))

        match escolha:
            case 1:
                m.exer_1()
            case 2:
                m.exer_2()
            case 3:
                m.exer_3()
            case 4:
                m.exer_4()
            case _:
                print('Numero invalido')
    except ValueError: 
        print('APENAS NUMEROS')

        
    
    desejo = input('Deseja continuar?(s/n):\n>> ').lower()

    if desejo == 's':
        clear = lambda: os.system('cls')
        clear()
    elif desejo == 'n':
        print('PROGRAMA ENCERRADO!')
        break
    else:
        print('Input invalido encerrando programa')
        break


