alunosPt1=['Carlos', 'Alessandra','Geraldo']
alunosPt2=['Guilherme','Paloma','Natan']
alunosPt3 = alunosPt1 + alunosPt2

#print(alunosPt3)

alunosPt1.extend(alunosPt2)

#print(alunosPt1)

# for + array
print(len(alunosPt1))

for i in alunosPt1:
    print(f'-{i} \n ###')