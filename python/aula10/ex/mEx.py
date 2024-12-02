from datetime import datetime
import calendar as c
from time import sleep as s
import random

def menu():
    print('-'*10,'-'*10)
    print('SELECIONE UM DOS EXERCICIOS')
    print('1 - Crie um cronômetro reverso com uma mensagem final personalizada usando o módulo time.')
    print('2 - Crie um programa que gere uma agenda semanal aleatória com atividades usando o módulo random.')
    print('3 - Use o módulo calendar para exibir o calendário completo do ano atual')
    print('4 - Use o módulo random para sortear um nome de uma lista de participantes.')
    print('-'*10,'-'*10)



def exer_1():
    try:
        segundo = int(input('Digite quanto segundos que você quer:\n>> '))
        mensg = input('Digite um mensagem:\n>> ')
    except ValueError:
        print('Alguma coisa deu errado verifique se você não colocou algo errado nos segundos')
    finally:

        for i in range(segundo,0,-1):
            s(1)
            print(f'{i} segundos')

        print(mensg)
        

def exer_2():
    semana = ['SEG','TER','QUA','QUI','SEX','SAB','DOM']
    tarefa = ['Levar o lixo fora','Comprar café','Pegar a carteira no detran','Comprar carne','Assistir filme','Yoga','Academia']
    
    semana_escolha = random.choice(semana)
    tarefa_escolha = random.choice(tarefa)

    return print(f'{semana_escolha,tarefa_escolha}')

def exer_3():
    mensagem = ['PUTA QUE PARIU VOCÊ SABE LER ?', 'ALGO DEU ERRADO']
    try:
        ano = int(input('Digite um ano:\n>>'))
        dia_atual = datetime.now().day
        mes_atual = datetime.now().month
        
        print(f'Você está no ano >> {ano}\nNo mês >> {mes_atual}\nNo dia >> {dia_atual}')
        print(c.calendar(ano))
    except ValueError:
        print(random.choice(mensagem))


def exer_4():
    try:
        participantes = []
        print('#'*3,'SORTEIO','#'*3)

        qt_par = int(input("quantas pessoas vão ser:\n>> "))
    except ValueError:
        print('SOMENTE NUMERO')
    finally:
        for part_a in range(qt_par):
            nome = input(f'Diga o nome do {part_a + 1}º participante:\n>> ')
            participantes.append(nome)

    part_sorte = random.choice(participantes) 

    return print(f'O sortudo foi: >>{part_sorte}<< PARABÉNS !!!!!')
