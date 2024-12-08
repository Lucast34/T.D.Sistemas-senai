import json as j
from os import system
import platform

limpar = platform.system()

def menu():
    print('-'*10)
    print('O que deseja fazer?')
    print('(1)-> Login')
    print('(2)-> Cadastro')
    print('-'*10)
def menu_escolha():
    ...


def limpar():
    if limpar == 'Windows':
        system('cls')
    
    elif limpar == 'Linux' or 'Darwin':
        system('clear')
