"""
Relações entre classes
Associação - Reaciona um objeto a outro
"""

class Usuario:
    def __init__(self,nome,login,senha):
        self.nome = nome
        self.login = login
        self.senha = senha
        self.livro = None
    
    # Property chama um objeto exerteno e retornando
    # 'Pego o objeto e retorno'
    @property
    def livroAdd(self):
        return self.livro

    # Pega o que foi retornando e acrescenta no atributo
    # 'Pego o que foi retornado e acrescentou no usuario'
    @livroAdd.setter
    def livroAdd(self,livroAdd):
        self.livro = livroAdd

class Livro:
    def __init__(self,nome,autor):
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
print(f"{user.livro }")