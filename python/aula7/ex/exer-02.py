"""
Duas lojas possuem estoques diferentes de produtos. 
Encontre os produtos disponíveis em ambas e os exclusivos de cada loja.
"""

Loja_a = {'Batata', 'Mandioca', 'Abóbora', 'Farinha de trigo', 'Ameixa', 'Banana','Maçã','Amora'}
Loja_b = {'Batata', 'Mandioca', 'Abóbora','Farinha de trigo','Nozes','Castanha', 'Açai', 'Blueberry','Cranberry'}

conj_Lab_u = Loja_a & Loja_b
conj_Lab_d = Loja_a - Loja_b
conj_Lab_db = Loja_b - Loja_a

print(conj_Lab_u)
print(conj_Lab_d)
print(conj_Lab_db)