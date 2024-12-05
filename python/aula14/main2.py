"""
Relações entre classes
Associação - Reaciona um objeto a outro
"""

class Usuario:
    def __init__(self,nome,login,senha) -> None:
        self.nome = nome
        self.login = login
        self.senha = senha
        self.biblioteca = None
    
    @property
    def livro(self):
        return self.biblioteca

    @livro.setter
    def AdicionarLivros(self,livro):
        self.biblioteca = livro

class Livro:
    def __init__(self,nome,autor) -> None:
        self.nome = nome
        self.autor = autor
    
    def mostrarAutor(self):
        return self.autor
        

user = Usuario('Victor','083983','senha')
book = Livro('place_holder','place_holder')

user.biblioteca=book
print(user.biblioteca.mostrarAutor())

# User
#  Livro
#   MostrarAutor

print(f"User {user.__dict__}\nLivro:{book.__dict__}")
print(f"{user.biblioteca}")