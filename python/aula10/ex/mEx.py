import datetime as dt
from datetime import date as da
import random

def exer_1():
    dt

def exer_2():
    semana = ['SEG','TER','QUA','QUI','SEX','SAB','DOM']
    tarefa = ['Levar o lixo fora','Comprar café','Pegar a carteira no detran','Comprar carne','Assistir filme','Yoga','Academia']
    
    semana_escolha = random.choice(semana)
    tarefa_escolha = random.choice(tarefa)

    return print(f'{semana_escolha,tarefa_escolha}')

def exer_3():
    caledario = da.strftime("%d/%m/%y")

    return caledario

def exer_4():
    participantes = []
    print('#'*3,'SORTEIO','#'*3)

    qt_par = int(input("quantas pessoas vão ser:\n>> "))

    for part_a in range(qt_par):
        nome = input(f'Diga o nome do {part_a + 1}º participante:\n>> ')
        participantes.append(nome)

    part_sorte = random.choice(participantes) 

    return print(f'O sortudo foi: >>{part_sorte}<< PARABÉNS !!!!!')
