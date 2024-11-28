'''
Crie um dicionário com informações sobre um aluno (por exemplo, nome, idade, notas). 
Em seguida, solicite ao usuário uma chave para acessar no dicionário. 
Caso a chave não exista, trate o erro e informe quais chaves estão disponíveis.
'''

alunos_dici = {
    'nome': 'fernando',
    'idade':'15',
    'nota':[4.5,5.5,6,8,8.6]
}

try:
    seleção = input('O quê deseja selecionar:\n>> ')

    print(f'{alunos_dici[seleção]}')
    
except KeyError as Error:
    print(f'Esse campo >>{Error}<< não existe.\nAqui está a lista dos campos existentes:\n{tuple(alunos_dici.keys())}')