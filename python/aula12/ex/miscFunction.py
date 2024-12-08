import json as j
from os import system
import platform

limpar = platform.system()

def menu():
    print('O deseja fazer?')
    print('1- Login')
    print('2- Cadastro')

def menu_escolha():
    ...


def limpar():
    if limpar == 'Windows':
        system('cls')
    
    elif limpar == 'Linux' or 'Darwin':
        system('clear')
