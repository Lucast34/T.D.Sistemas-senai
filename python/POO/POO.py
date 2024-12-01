class Item:
	def __init__(self, name):
		#print(f"an instance created {name}")
		# criando instance
		self.name = name
		self.price = price
		self.quantity = quantity
		
	def caulate_total(self,x,y):
		 return x * y

item1 = Item('Phone',100,5)

#Não é mais necessario
#item1.name = 'Phone'
#item1.price = 100
#item1.quantity = 5

#print(item1.calculate_total(item1.price,item1.quantity))

item2 = Item('Laptop',1000,3)

#item2.name = 'Laptop'
#item2.price = 1000
#item2.quantity = 3

#print(item2.calculate_total(item2.price,item2.quantity))
