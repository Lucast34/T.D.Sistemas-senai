# (^-^)
import json as j
from os import system
import platform

limpar = platform.system()
emote = platform.system()

def menu():
    print(platform.system())
    print('-'*10)
    print('O que deseja fazer?')
    print('(1)-> Login')
    print('(2)-> Cadastro')
    print('-'*10)
def menu_escolha():
    ...

def limpar():
    
    system('cls') if limpar == 'win32' or 'Windows' else system('clear')


def emot():
    emotes = '(^o^)' if emote == 'win32' or 'Windows' else '(^-^)'
    
    return emotes