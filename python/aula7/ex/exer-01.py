'''
Encontrar alunos que cursam apenas uma disciplina dado as disciplinas:
-matematica com os nomes dos alunos que fazem Matemática
-fisica com os nomes dos alunos que fazem Física
'''

matematica = {'Lorena','Breno','Matheus','Daniel','Enzo','Andre','Felipe','Maria'}
fisica = {'Laura','Nilce','Gabriel','Ana','Felipe','Enzo','Andre','Karina'}

conj_mf = matematica ^ fisica

print(f'Alunos que só curso apenas disciplina:')

for i in conj_mf:
    print(f'>> {i}')

'''
correção
'''
