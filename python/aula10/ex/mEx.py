import datetime as dt
import random

def exer_1():
    dt

def exer_2():
    semana = ['SEG','TER','QUA','QUI','SEX','SAB','DOM']
    tarefa = ['Levar o lixo fora','Comprar café','Pegar a carteira no detran','Comprar carne','Assistir filme','Yoga','Academia']
    
    semana_escolha = random.choice(semana)
    tarefa_escolha = random.choice(tarefa)

    return(f'{semana_escolha,tarefa_escolha}')


print(exer_2())