import json as j
from os import system
import platform

limpar = platform.system()


def limpar():
    if limpar == 'Windows':
        system('cls')
    
    elif limpar == 'Linux' or 'Darwin':
        system('clear')


def cadastro():
   print('Área de cadastro')
   u_nome = input('Digite o seu nome >> ')
   user = input('Digite um usuario >> ')
   u_senha = input('Digite uma senha >> ') 


cadastro()

limpar()