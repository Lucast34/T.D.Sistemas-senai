# (^-^)
import random
import json
from os import system, path



#exercicio 1
def classificar_idade():
    print('Por favor informe a sua idade ')
    idade = int(input(">> "))


    if idade < 12:
        print('Criança') 
    elif idade <= 17:
        print('Adolecente')
    else:
        print('Adulto')


# exerciocio 2


estoque_dicio = {
    'nome_p' : ['banana'] ,
    'qt.p' : [5]
    }




def estoque():
    while True:
        try:
            print('-'*10,'ESTOQUE','-'*10)
            print('1 - Adicionar produto e a quantidade')
            print('2 - Adicionar verificar produtos que tem no estoque')
            print('3 - Atualizar um produtor')
            print('0 - Para sair do programa')

            escolha = int(input('O que deseja faze ?\n>>'))
        
            match escolha:
                case 1:
                    add_produto = input('') .strip()
                    estoque_dicio['nome_p'].append(add_produto)
                    
                    add_qt_produto = int(input(''))
                    
                    print('valor invalido')if add_qt_produto == 0 else estoque_dicio['qt.p'].append(add_qt_produto)
                    
                case 2:
                    print(list(estoque_dicio['nome_p']))
                    print(list(estoque_dicio['qt.p']))

                case 3:
                    produto_atu = input('')
                    qt_atu = int(input(''))
                    
                    estoque_dicio.update({
                        'nome_p' : produto_atu ,
                        'qt.p' : qt_atu
                    })
                case _:
                    print('Program finalizado')
                    break
        except ValueError:
                    print('Houve um error')



estoque()

#ex3

def adivinhar():
    numero = []
    tentaiva = 0
    
    num_ran=random.randrange(0,101,1)
    
    numero.append(num_ran)

    print(numero)

    while True:
        
        print('tente adivinhar o numero')
    
        nu_input = int(input('>> '))

        if nu_input < num_ran :
            print('muito baixo')
        elif nu_input > num_ran:
            print('Muito alto')
        else:
            print('parabéns')
            break
        
        tentaiva += 1

        if tentaiva > 5: 
            print(f'game over o número era: {numero}') 
            break
        else: 
            print (tentaiva) 


# ex4

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade
        self.livros = []  # Lista para armazenar os livros

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def __str__(self):
        return f'Autor: {self.nome}, Nacionalidade: {self.nacionalidade}'


class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

    def __str__(self):
        return f'Título: {self.titulo}, Ano: {self.ano}, Autor: {self.autor.nome}'


autor = Autor("Machado de Assis", "Brasileira")


livro1 = Livro("Dom Casmurro", 1899, autor)

autor.adicionar_livro(livro1)


print(autor)
print("Livros do autor:")
for livro in autor.livros:
    print(livro)

# ex5
link_arquivo = '.\prova\\arquivo_da_prova.json'

def calculadora():

    calculo = {
        'operacao': [],
        'num1': [],
        'num2': [],
        'resultado': []
    }
    system('cls')
    if not path.exists(link_arquivo):
        with open(link_arquivo, 'a', encoding='utf-8') as resposta:
            json.dump(
                calculo,
                resposta
            )
    with open(link_arquivo, 'r') as resposta:
        results = json.load(resposta)
    operandos = ['+', '-', '*', '/']
    print('==' * 10, 'CALCULADORA', '==' * 10)
    def salvar(result, operacao, num1, num2):
        results['operacao'].append(operacao)
        results['resultado'].append(result)
        results['num1'].append(num1)
        results['num2'].append(num2)
        with open(link_arquivo, 'w', encoding='utf-8') as resposta:
            json.dump(
                results,
                resposta
            )
        print('\033[32mO calculo foi salvo com sucesso!\033[m')
    def calculadora(operacao):
        result = 0
        try:
            num2 = float(input('Informe o segundo número: '))
            match operacao:
                case '+':
                    result = num1 + num2
                    print(f'O resultado é: {result}') 
                case '-':
                    result = num1 - num2
                    print(f'O resultado é: {result}')
                case '*':
                    result = num1 * num2
                    print(f'O resultado é: {result}')
                    
                case '/':
                    result = num1 / num2
                    print(f'O resultado é: {result}')
            
        except ZeroDivisionError:
            print('Não é possível realizar uma divisão por 0')
            result = 'Divisão por 0'
        
        salvar(result, operacao, num1, num2)
    def exibir():
        op = ''
        op += '('
        for i in operandos:
            op += f'{i} '
        op += '): '
        return op
    num1 = float(input('Informe o primeiro número: '))
    op = input(f'Informe a operação: {exibir ()} ')
    for i in operandos:
        if op == i:
            calculadora(op)
            break