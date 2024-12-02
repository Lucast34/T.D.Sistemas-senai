from ex import modulo_aula1 as m


while True:
    escolha = int(input("escolha um dos exercicios"))
    
    match escolha:
        case 1:
            m.dicio()
        case 2:
            m.calc_nasc()
        case _:
            print('Programa encerrado')
            break
    
    esco_if = input('Deseja continuar?(s/n)\n>> ')
    
    if esco_if == 's':
        print('Ok :)')
    elif esco_if == 'n':
        print('Programa encerrado')
        break