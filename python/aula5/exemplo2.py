def soma(x , y, z):
    if z is not None:
        print(f'{x}, {y} , {z} / {x + y + z}')
    else:
        print('Z Não exite')

soma(4,8,10)
soma(y=3,z=1,x=4)
soma(7,2,z= None)