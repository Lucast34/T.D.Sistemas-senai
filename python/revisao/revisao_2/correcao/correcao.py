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

class Aluno:
    def __init__(self, nome):
        self.nome = nome 
        self._notas = []
        
    def adicionarNotas(self,nota):
        self._notas.append(nota)