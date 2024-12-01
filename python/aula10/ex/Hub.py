import mEx as m

print('-'*10,'-'*10)
print('SELECIONE UM DOS EXERCICIOS')
print('1 - Crie um cronômetro reverso com uma mensagem final personalizada usando o módulo time.')
print('2 - Crie um programa que gere uma agenda semanal aleatória com atividades usando o módulo random.')
print('3 - Use o módulo calendar para exibir o calendário completo do ano atual')
print('4 - Use o módulo random para sortear um nome de uma lista de participantes.')
print('-'*10,'-'*10)

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