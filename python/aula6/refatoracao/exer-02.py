'''
2. Agenda de Contatos
Crie um programa para armazenar números de telefone. O usuário deve poder adicionar novos contatos (nome como chave e número como valor). 
Depois, o programa deve exibir todos os contatos cadastrados. 
Obs: O salvamento deverá parar apenas quando o usuário digitar "finalizar"
'''

agenda={

}

while True:
    try:
        confirmar = input('Deseja adicionar um contato?(sim||nao)\n>>>').lowe()
        
        if confirmar != 'sim' and confirmar != 'nao':
            print('\033[31mError input invalido\033[m,digite sim ou não.')

        elif  confirmar == 'nao' or confirmar != 'sim':
            break

        
        elif confirmar == 'sim':
            nome = input('Digite o nome do usuário:')

            telefone = input(f'Digite o telefone do usuário {nome}:')

            print('*'*10)
            
            agenda.update({
                nome : telefone 
            })


            final = input('Deseja finalizar?\n>>')
            
            if final == 'sim':
                break
    except:
        print('\033[31mError input invalido\033[m,digite sim ou não.')

print('-'*5,'Agenda Eletronica','-'*5)    
for contatinho in agenda.items():
    print(f'Nome:{contatinho[0]} - Número:{contatinho[1]}')

