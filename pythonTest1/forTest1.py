my = {n for n in range(1,6)}
print(my, type(my))

data = [('aa',10),('bb',20),('cc',30)]
my = { k:v for k,v in data }
print(my, type(my))

my = ( n for n in range(1,6)) # tuple(X)
print(my, type(my))
