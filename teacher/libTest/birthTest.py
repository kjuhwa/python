fp = open('births.txt','r')

mList =[]
for rd in fp:
    y,m,f = rd.split(',')
    mList.append( int(m))

print( mList)
print( sum( mList) )
