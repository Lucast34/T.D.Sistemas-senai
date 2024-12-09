"""
1- criar o aluno (obj) nome e notas
2- metodo do aluno calcular media
3- verificar se ele passou ou não
4- calcular media, criar obj
5- verificar se existe alunos anteriores
6- exportar para um json
"""
# sem under - publico
# com um under - protegido
# com dois under - privado 

import json as j
import os


class Aluno:
    def __init__(self, nome):
        self.nome = nome 
        self._notas = []
        
    def adicionarNotas(self,nota):
        # [(lambda x : x*x )(x)for x in range(4)] ← refatorção

        self._notas.append(nota)

    def calcularMedia(self):
        return sum(self._notas)/len(self._notas) if self._notas else  0

    def Apr(self):
        media = self.calcularMedia()
        
        return 'Aprovado' if media >= 7 else 'Reprovado' 

    def exportAluno(self):
        dados_alunos = {
            'nome' : self.nome,
            'notas' : self._notas,
            'media' :   self.calcularMedia(),
            'aprovacao' : self. Apr()
        }
        
        caminho = ''
        
        if os.path.exist('dadosAlunos.json'): # 
            with open('dadosAlunos.json','r',encoding='utf8') as arquivo:
                try:
                    dados = j.load(arquivo)
                except j.JSONDecodeError:
                    dados = []
        else:
            dados = []

        dados.append(dados_alunos)

        with open('dadosAlunos','w',encoding='utf8') as arquivos:
            j.dump(dados,indent=2)


aluno1 = Aluno('Victor') 

aluno1.adicionarNotas(8)
aluno1.adicionarNotas(5)

aluno1.Apr()

print(aluno1._notas)

aluno2 = Aluno('Bruna')